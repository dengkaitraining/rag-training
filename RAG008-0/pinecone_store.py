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