import json
import os
import time
from pathlib import Path
from dotenv import load_dotenv
from pinecone import Pinecone

# 取得目前檔案目錄的絕對路徑，確保讀取 .env 不會因為執行位置不同而失敗
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

        # 建立 Pinecone 客戶端與 Index 實例
        self.pc = Pinecone(api_key=self.api_key)
        self._ensure_index_exists()
        self.index = self.pc.Index(self.index_name)

    def _ensure_index_exists(self):
        """檢查並建立 Index（私有輔助方法）"""
        if not self.pc.has_index(self.index_name):
            print(f"正在建立 Index: {self.index_name} ...")
            self.pc.create_index_for_model(
                name=self.index_name,
                cloud=self.cloud,
                region=self.region,
                embed={
                    "model": self.embed_model,
                    "field_map": {"text": "chunk_text"}
                }
            )
            print("Index 建立完成。")

    def build_vector_database(self, json_path: Path):
        """
        讀取外部 JSON 檔並批次寫入（Upsert）至 Pinecone 向量資料庫
        :param json_path: JSON 檔案的 Path 物件
        """
        file_path = Path(json_path).resolve()
        if not file_path.exists():
            raise FileNotFoundError(f"找不到指定的 JSON 檔案：{file_path}")

        print(f"正在從 {file_path} 讀取資料...")
        with open(file_path, "r", encoding="utf-8") as f:
            records = json.load(f)

        print(f"寫入 {len(records)} 筆資料至 Namespace '{self.namespace}'...")
        self.index.upsert_records(
            namespace=self.namespace,
            records=records
        )
        print("資料已成功寫入 Pinecone！")

        # 等待同步 (Eventual Consistency)
        print("等待資料庫同步中 (5秒)...")
        time.sleep(5)

        stats = self.index.describe_index_stats()
        print("\n[最新 Index 統計資料]")
        print(stats)

    def search_vector_database(self, query: str, top_k: int = 3):
        """
        搜尋向量資料庫並列印格式化結果
        :param query: 搜尋問題或關鍵字
        :param top_k: 傳回最相關的資料筆數
        """
        print(f"\n[搜尋問題]：{query}")
        print("=" * 60)

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
        if not hits:
            print("未找到相關資料。")
            return

        for hit in hits:
            fields = hit.fields or {}
            print(f"ID  ：{hit.id}")
            print(f"分數：{hit.score:.4f}")
            print(f"內容：{fields.get('chunk_text', 'N/A')}")
            print(f"分類：{fields.get('category', 'N/A')}")
            print(f"來源：{fields.get('source', 'N/A')}")
            print("-" * 60)