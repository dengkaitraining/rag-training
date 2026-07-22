## Prompt 1. 依據上述輸出結果建立 Python Flask 網站。
```markdown
# 依據 <oop_1>與<oop_2> python class 、<env>、<data> 資訊編寫一個 RAG 檢索增強生成搜尋 Python Flask Web Application，規格如<spec>所述。
<spec>
  1. 將 <oop_1> 內 RAG Knowledge Base 以 <oop_2> 的 vector databease 代替，將 <oop_2> 取得的 <chunk_text> 組合成 <oop_1> 內 RAG <context> 資訊。
  2. 呈現查尋問題結果的頁面是動態頁面。
  3. 前端不使用CSS，也不使用Javascript。
</spec>

<oop_1>
import os
import re
from pathlib import Path
import markdown
import requests
from dotenv import load_dotenv

# 讀取當前檔案所在目錄的 .env 檔案
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


class KnowledgeBase:
    """處理知識庫檔案讀取與檢索的類別"""

    def __init__(self, file_path: str = "knowledge.txt"):
        # 使用 pathlib.Path 確保檔案使用絕對路徑
        self.file_path = (BASE_DIR / file_path).resolve()
        self.line_pattern = re.compile(r'^\s*([^,]+?)\s*,\s*"(.*?)"\s*$')

    def find_by_keyword(self, keyword: str) -> list[str]:
        """從知識庫檔案中檢索關鍵字描述"""
        results = []

        if not self.file_path.exists():
            print(f"提示：找不到檔案 {self.file_path}")
            return results

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, 1):
                    line = line.strip()
                    if not line:
                        continue

                    match = self.line_pattern.match(line)
                    if match:
                        parsed_keyword = match.group(1)
                        description = match.group(2)

                        if parsed_keyword.lower() == keyword.lower():
                            results.append(description)
                    else:
                        print(f"警告：第 {line_number} 行格式不符，已跳過：{line}")

        except IOError as e:
            print(f"讀取檔案時發生錯誤: {e}")

        return results


class RAGService:
    """整合 RAG 流程與 API 呼叫的服務類別"""

    def __init__(self, knowledge_base: KnowledgeBase):
        self.kb = knowledge_base
        # 1. 讀取 .env 中的 API_KEY
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("找不到 GEMINI_API_KEY，請先在 .env 設定環境變數！")

        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"
        self.keyword_pattern = re.compile(
            r"(?<![a-zA-Z])(AI|IoT|Blockchain|AR|VR)(?![a-zA-Z])",
            flags=re.IGNORECASE,
        )

    def extract_keywords(self, user_prompt: str) -> list[str]:
        """萃取用戶提問中的技術關鍵字"""
        return self.keyword_pattern.findall(user_prompt)

    @staticmethod
    def markdown_to_html(md_text: str) -> str:
        """Markdown 轉 HTML"""
        return markdown.markdown(
            md_text, extensions=["extra", "codehilite", "toc"]
        )

    def process_query(self, user_prompt: str) -> str:
        """處理查詢的核心主邏輯"""
        matches = self.extract_keywords(user_prompt)
        if not matches:
            return "<H1>你的問題太高深了，本仙人功力不足以回答。</H1><a href='/'>回提問頁</a>"

        search_str = matches[0]

        # 檢索知識庫
        ai_results = self.kb.find_by_keyword(search_str)
        context_str = "。".join(ai_results)

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

        response = requests.post(
            self.api_url, headers=headers, json=data, timeout=15
        )
        response.raise_for_status()

        result = response.json()
        raw_text = result["candidates"][0]["content"]["parts"][0]["text"]

        return self.markdown_to_html(raw_text)


# Flask App 整合範例 (可視情況取消註解或獨立放於 app.py)
"""
from flask import Flask, render_template, request

app = Flask(__name__)
rag_service = RAGService(KnowledgeBase("knowledge.txt"))

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/process", methods=["POST"])
def process():
    user_prompt = request.form.get("user_prompt", "")
    outstr = rag_service.process_query(user_prompt)
    return render_template("output.html", user_prompt=user_prompt, result=outstr)
"""
</oop_1>

<oop_2>
import json
import os
import time
from pathlib import Path
from dotenv import load_dotenv
from pinecone import Pinecone

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(dotenv_path=BASE_DIR / ".env")


class PineconeVectorStore:
    def __init__(self):
        """初始化 Pinecone Client 與載入環境變數"""
        self.api_key = os.getenv("PINECONE_API_KEY")
        if not self.api_key:
            raise ValueError("找不到 PINECONE_API_KEY，請確認 .env 設定。")

        self.index_name = os.getenv("PINECONE_INDEX_NAME", "course-rag-demo")
        self.namespace = os.getenv("PINECONE_NAMESPACE", "ai-course")
        self.cloud = os.getenv("PINECONE_CLOUD", "aws")
        self.region = os.getenv("PINECONE_REGION", "us-east-1")
        self.embed_model = os.getenv("PINECONE_EMBED_MODEL", "llama-text-embed-v2")

        self.pc = Pinecone(api_key=self.api_key)
        self._ensure_index_exists()
        self.index = self.pc.Index(self.index_name)

    def _ensure_index_exists(self):
        """檢查並建立 Index（私有輔助方法）"""
        if not self.pc.has_index(self.index_name):
            self.pc.create_index_for_model(
                name=self.index_name,
                cloud=self.cloud,
                region=self.region,
                embed={
                    "model": self.embed_model,
                    "field_map": {"text": "chunk_text"}
                }
            )

    def validate_records(self, records):
        """檢查寫入資料格式是否符合 Pinecone 需求"""
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
        self.index.upsert_records(
            namespace=self.namespace,
            records=records
        )
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

    def search_vector_database(self, query: str, top_k: int = 3):
        """搜尋向量資料庫並傳回結構化結果 list"""
        results = self.index.search(
            namespace=self.namespace,
            query={
                "top_k": top_k,
                "inputs": {
                    "text": query
                }
            },
            fields=["chunk_text", "category", "source"]
        )

        hits = results.result.hits
        formatted_results = []
        
        if hits:
            for hit in hits:
                fields = hit.fields or {}
                formatted_results.append({
                    "id": hit.id,
                    "score": round(hit.score, 4),
                    "chunk_text": fields.get("chunk_text", "N/A"),
                    "category": fields.get("category", "N/A"),
                    "source": fields.get("source", "N/A")
                })

        return formatted_results
</oop_2>

<env>
GEMINI_API_KEY=
PINECONE_API_KEY=
PINECONE_INDEX_NAME=course-rag-demo-2
PINECONE_NAMESPACE=ai-course
PINECONE_CLOUD=aws
PINECONE_REGION=us-east-1
PINECONE_EMBED_MODEL=llama-text-embed-v2
</env>

<data>
[
  {
    "_id": "doc-001",
    "chunk_text": "RAG 是結合資訊檢索與大型語言模型的生成式人工智慧技術。",
    "category": "RAG",
    "source": "AI課程第一章"
  },
  {
    "_id": "doc-002",
    "chunk_text": "向量資料庫可根據語意相似度搜尋與問題最相關的文件。",
    "category": "VectorDB",
    "source": "AI課程第二章"
  },
  {
    "_id": "doc-003",
    "chunk_text": "AI Agent 可以使用工具、存取資料，並根據目標執行多個步驟。",
    "category": "Agent",
    "source": "AI課程第三章"
  },
  {
    "_id": "doc-004",
    "chunk_text": "Flask 是一個輕量級的 Python Web Application Framework。",
    "category": "Python",
    "source": "Python課程"
  },
  {
    "_id": "doc-005",
    "chunk_text": "Pinecone 是雲端託管的向量資料庫，可應用於語意搜尋與 RAG。",
    "category": "VectorDB",
    "source": "AI課程第二章"
  }
]
</data>
```

```markdown
# 1. 請將 class PineconeVectorStore 與 class RAGService 的程式與主程式分開，並加入詳細的說明內容「comments」，讓程式維護人員更容易閱讀。
# 2. 當搜尋 vector database 未找到 chunk_text 後續不需要再與 LLM 提問，值節回覆「無相關資料」等資訊內容。
# 3. 在 console 下 print 所有操作序息，並建立一個 console_flag 可開啟或關閉此功能。
```