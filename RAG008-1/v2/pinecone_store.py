import json
import os
import time
from pathlib import Path
from dotenv import load_dotenv
from pinecone import Pinecone

# 取得當前檔案目錄並載入環境變數
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


class PineconeVectorStore:
    """
    Pinecone 向量資料庫操作服務類別
    負責 Index 的初始化、資料格式驗證、向量資料寫入與語意搜尋。
    """

    def __init__(self, console_flag: bool = True):
        """
        初始化 Pinecone Client 並讀取環境變數配置

        :param console_flag: 控制是否在 Console 印出操作訊息 (預設 True 開啟)
        """
        self.console_flag = console_flag
        self._log("=== [PineconeVectorStore] 初始化開始 ===")

        self.api_key = os.getenv("PINECONE_API_KEY")
        if not self.api_key:
            raise ValueError("找不到 PINECONE_API_KEY，請確認 .env 檔案中的設定。")

        # 讀取 Pinecone 相關設定（提供預設值）
        self.index_name = os.getenv("PINECONE_INDEX_NAME", "course-rag-demo-2")
        self.namespace = os.getenv("PINECONE_NAMESPACE", "ai-course")
        self.cloud = os.getenv("PINECONE_CLOUD", "aws")
        self.region = os.getenv("PINECONE_REGION", "us-east-1")
        self.embed_model = os.getenv("PINECONE_EMBED_MODEL", "llama-text-embed-v2")

        self._log(f"環境參數 -> Index: {self.index_name} | Namespace: {self.namespace} | Model: {self.embed_model}")

        # 建立 Pinecone 實例並確保 Index 存在
        self.pc = Pinecone(api_key=self.api_key)
        self._ensure_index_exists()
        self.index = self.pc.Index(self.index_name)
        self._log("=== [PineconeVectorStore] 初始化完成 ===\n")

    def _log(self, message: str):
        """[私有方法] 控制 Console 訊息列印的統一通道"""
        if self.console_flag:
            print(message)

    def _ensure_index_exists(self):
        """[私有方法] 檢查指定的 Index 是否已建立；若不存在則自動創建對應的服務 Index"""
        self._log(f"檢查 Pinecone Index [{self.index_name}] 是否存在...")
        if not self.pc.has_index(self.index_name):
            self._log(f"Index [{self.index_name}] 不存在，正在創建中...")
            self.pc.create_index_for_model(
                name=self.index_name,
                cloud=self.cloud,
                region=self.region,
                embed={
                    "model": self.embed_model,
                    "field_map": {"text": "chunk_text"},  # 將 chunk_text 欄位進行向量化
                },
            )
            self._log(f"Index [{self.index_name}] 創建完成！")
        else:
            self._log(f"Index [{self.index_name}] 已存在。")

    def validate_records(self, records: list) -> bool:
        """
        驗證欲寫入向量資料庫的 JSON 紀錄格式是否符合規範

        :param records: 包含文檔資料的 List
        :return: 驗證通過傳回 True，失敗則拋出 ValueError
        """
        self._log(f"開始驗證寫入資料格式 (共 {len(records) if isinstance(records, list) else 0} 筆)...")
        if not isinstance(records, list):
            raise ValueError("輸入資料格式必須是 List (陣列)。")
        if len(records) == 0:
            raise ValueError("輸入資料內容不得為空陣列。")

        for idx, item in enumerate(records):
            if not isinstance(item, dict):
                raise ValueError(f"第 {idx + 1} 筆資料格式不正確，必須是 Dict (物件)。")
            if "_id" not in item or not item["_id"]:
                raise ValueError(f"第 {idx + 1} 筆資料缺少必填欄位 '_id'。")
            if "chunk_text" not in item or not item["chunk_text"]:
                raise ValueError(f"第 {idx + 1} 筆資料缺少必填欄位 'chunk_text'。")
        
        self._log("資料格式驗證成功！")
        return True

    def build_vector_database_from_records(self, records: list):
        """
        將驗證過的資料串流上傳至 Pinecone 向量資料庫中

        :param records: 資料列表
        :return: (寫入資料筆數, Index 統計資訊)
        """
        self.validate_records(records)
        self._log(f"正在將 {len(records)} 筆紀錄 Upsert 至 Namespace [{self.namespace}]...")
        self.index.upsert_records(namespace=self.namespace, records=records)
        
        self._log("等待 3 秒鐘以確保 Pinecone 索引資料同步...")
        time.sleep(3)
        
        stats = self.index.describe_index_stats()
        self._log(f"資料 Upsert 完成！目前 Index 統計資訊: {stats}")
        return len(records), stats

    def build_vector_database(self, json_path: Path):
        """
        讀取指定的 JSON 檔案並寫入 Pinecone 向量資料庫

        :param json_path: JSON 檔案路徑
        """
        file_path = Path(json_path).resolve()
        self._log(f"讀取資料庫 JSON 檔案: {file_path}")
        if not file_path.exists():
            raise FileNotFoundError(f"找不到指定的 JSON 檔案：{file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            records = json.load(f)

        return self.build_vector_database_from_records(records)

    def search_vector_database(self, query: str, top_k: int = 3) -> list[dict]:
        """
        搜尋向量資料庫，並傳回與 Query 最相關的 top_k 筆結構化結果

        :param query: 檢索的文字問題
        :param top_k: 回傳最相似的結果數量
        :return: 包含相似度分數與內容的列表
        """
        self._log(f"=== [Vector Search] 開始搜尋 ===")
        self._log(f"檢索 Query: '{query}' | Top K: {top_k} | Namespace: {self.namespace}")

        results = self.index.search(
            namespace=self.namespace,
            query={"top_k": top_k, "inputs": {"text": query}},
            fields=["chunk_text", "category", "source"],
        )

        hits = results.result.hits
        formatted_results = []

        if hits:
            self._log(f"搜尋成功，共找到 {len(hits)} 筆命中紀錄：")
            for idx, hit in enumerate(hits, 1):
                fields = hit.fields or {}
                chunk_text = fields.get("chunk_text", "N/A")
                score = round(hit.score, 4)
                self._log(f"  [{idx}] ID: {hit.id} | Score: {score} | Content: {chunk_text}")
                
                formatted_results.append(
                    {
                        "id": hit.id,
                        "score": score,
                        "chunk_text": chunk_text,
                        "category": fields.get("category", "N/A"),
                        "source": fields.get("source", "N/A"),
                    }
                )
        else:
            self._log("搜尋結果：未找到任何相關的向量紀錄。")

        self._log(f"=== [Vector Search] 搜尋結束 ===\n")
        return formatted_results