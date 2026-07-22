import json
import os
import time
from pathlib import Path
import markdown
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request
from pinecone import Pinecone

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


class PineconeVectorStore:
    """向量資料庫類別（替代原本的 KnowledgeBase）"""

    def __init__(self):
        self.api_key = os.getenv("PINECONE_API_KEY")
        if not self.api_key:
            raise ValueError("找不到 PINECONE_API_KEY，請確認 .env 設定。")

        self.index_name = os.getenv("PINECONE_INDEX_NAME", "course-rag-demo-2")
        self.namespace = os.getenv("PINECONE_NAMESPACE", "ai-course")
        self.cloud = os.getenv("PINECONE_CLOUD", "aws")
        self.region = os.getenv("PINECONE_REGION", "us-east-1")
        self.embed_model = os.getenv("PINECONE_EMBED_MODEL", "llama-text-embed-v2")

        self.pc = Pinecone(api_key=self.api_key)
        self._ensure_index_exists()
        self.index = self.pc.Index(self.index_name)

    def _ensure_index_exists(self):
        """檢查並建立 Index"""
        if not self.pc.has_index(self.index_name):
            self.pc.create_index_for_model(
                name=self.index_name,
                cloud=self.cloud,
                region=self.region,
                embed={
                    "model": self.embed_model,
                    "field_map": {"text": "chunk_text"},
                },
            )

    def validate_records(self, records):
        """檢查寫入資料格式"""
        if not isinstance(records, list):
            raise ValueError("JSON 內容必須是 List (陣列) 格式。")
        if len(records) == 0:
            raise ValueError("JSON 內容不得為空陣列。")

        for idx, item in enumerate(records):
            if not isinstance(item, dict):
                raise ValueError(f"第 {idx+1} 筆資料格式不正確，必須是物件 (Dict)。")
            if "_id" not in item or not item["_id"]:
                raise ValueError(f"第 {idx+1} 筆資料缺少必填欄位 '_id'。")
            if "chunk_text" not in item or not item["chunk_text"]:
                raise ValueError(f"第 {idx+1} 筆資料缺少必填欄位 'chunk_text'。")
        return True

    def build_vector_database_from_records(self, records: list):
        """將驗證過的 records 寫入向量資料庫"""
        self.validate_records(records)
        self.index.upsert_records(namespace=self.namespace, records=records)
        time.sleep(3)  # 等待同步
        stats = self.index.describe_index_stats()
        return len(records), stats

    def build_vector_database(self, json_path: Path):
        """讀取外部 JSON 檔並寫入向量資料庫"""
        file_path = Path(json_path).resolve()
        if not file_path.exists():
            raise FileNotFoundError(f"找不到指定的 JSON 檔案：{file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            records = json.load(f)

        return self.build_vector_database_from_records(records)

    def search_vector_database(self, query: str, top_k: int = 3) -> list[dict]:
        """搜尋向量資料庫並傳回結構化結果 list"""
        results = self.index.search(
            namespace=self.namespace,
            query={"top_k": top_k, "inputs": {"text": query}},
            fields=["chunk_text", "category", "source"],
        )

        hits = results.result.hits
        formatted_results = []

        if hits:
            for hit in hits:
                fields = hit.fields or {}
                formatted_results.append(
                    {
                        "id": hit.id,
                        "score": round(hit.score, 4),
                        "chunk_text": fields.get("chunk_text", "N/A"),
                        "category": fields.get("category", "N/A"),
                        "source": fields.get("source", "N/A"),
                    }
                )

        return formatted_results


class RAGService:
    """整合 RAG 流程與 API 呼叫的服務類別"""

    def __init__(self, vector_store: PineconeVectorStore):
        self.vector_store = vector_store
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("找不到 GEMINI_API_KEY，請先在 .env 設定環境變數！")

        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

    @staticmethod
    def markdown_to_html(md_text: str) -> str:
        """Markdown 轉 HTML"""
        return markdown.markdown(
            md_text, extensions=["extra", "codehilite", "toc"]
        )

    def process_query(self, user_prompt: str) -> str:
        """處理查詢的核心主邏輯"""
        if not user_prompt.strip():
            return "<h1>請輸入有效的查詢問題。</h1><a href='/'>回提問頁</a>"

        # 規格 1：從 Vector Database 檢索，並將取得的 chunk_text 組合成 context
        search_results = self.vector_store.search_vector_database(
            user_prompt, top_k=3
        )

        chunk_texts = [
            item["chunk_text"]
            for item in search_results
            if item.get("chunk_text") != "N/A"
        ]

        if not chunk_texts:
            context_str = "無相關資料"
        else:
            context_str = "。".join(chunk_texts)

        # 組裝 Prompt
        system_prompt = (
            f"<user_prompt>{user_prompt}</user_prompt>"
            f"<context>{context_str}</context>"
            f"<specifier>從context找出user_prompt的答案，如果找不到就說不知道</specifier>"
        )

        # 呼叫 Gemini API
        headers = {
            "Content-Type": "application/json",
            "X-goog-api-key": self.api_key,
        }
        data = {"contents": [{"parts": [{"text": system_prompt}]}]}

        try:
            response = requests.post(
                self.api_url, headers=headers, json=data, timeout=15
            )
            response.raise_for_status()
            result = response.json()
            raw_text = result["candidates"][0]["content"]["parts"][0]["text"]
            return self.markdown_to_html(raw_text)
        except Exception as e:
            return f"<h1>系統呼叫發生錯誤：{str(e)}</h1><a href='/'>回提問頁</a>"


# 初始化 Flask 應用與 RAG 服務
app = Flask(__name__)

# 初始化 Vector Store 並自動寫入 data
vector_store = PineconeVectorStore()
data_json_path = BASE_DIR / "knowledge.json"
if data_json_path.exists():
    try:
        vector_store.build_vector_database(data_json_path)
        print("已成功初始化與寫入知識庫至 Pinecone。")
    except Exception as e:
        print(f"寫入 Pinecone 時出錯或已存在資料：{e}")

rag_service = RAGService(vector_store)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    user_prompt = request.form.get("user_prompt", "")
    outstr = rag_service.process_query(user_prompt)
    # 規格 2：呈現查詢結果的頁面為動態頁面 (使用 Jinja2 渲染帶有變數的 output.html)
    return render_template("output.html", user_prompt=user_prompt, result=outstr)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)