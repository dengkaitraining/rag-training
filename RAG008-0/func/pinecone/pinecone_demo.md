## Prompt 1. 
&lt;code&gt; 的代碼是將Data Chunk 的Embedding Vector存到Pinecone的向量資料庫，然後進行檢索。完成將 &lt;code&gt; 代碼分成2個可獨立執行的.py程式，一個負責向量資料庫的建立，一個負責檢索。 &lt;code&gt; ...&lt;/code&gt; 

```markdown
# 1. <code> 代碼是將Data Chunk 的Embedding Vector存到Pinecone的向量資料庫，然後進行檢索。
# 2. 完成將<code>代碼分成2個主要的 function，依據 <spec> 建立與 python 物件導向的規範，封裝為 class。
# 3. 另外產生呼叫 class 測試的 CLI 建立 vector database 與 搜尋 vector database 的輸入界面。
<spec>
 1. build vector database function : 
    - create_index_for_model 的參數透過 .env 檔案儲存參數。
    - 準備要儲存的文字 records 從外部 json 檔案載入。
 2. search vector database function : 
    - 顯示搜尋結果。
 3. 檔案讀取使用 from pathlib import Path 讀取絕對路徑。
</spec>
<code>
import os
import time
from dotenv import load_dotenv
from pinecone import Pinecone

# 讀取 .env
load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")

if not api_key:
    raise ValueError("找不到 PINECONE_API_KEY，請確認 .env 設定。")

# 建立 Pinecone Client
pc = Pinecone(api_key=api_key)

index_name = "course-rag-demo"
namespace = "ai-course"

# --------------------------------------------------
# 1. 建立具備 Integrated Embedding 的 Index
# --------------------------------------------------
if not pc.has_index(index_name):
    pc.create_index_for_model(
        name=index_name,
        cloud="aws",
        region="us-east-1",
        embed={
            "model": "llama-text-embed-v2",
            "field_map": {
                "text": "chunk_text"
            }
        }
    )

# 連接 Index
index = pc.Index(index_name)

# --------------------------------------------------
# 2. 準備要儲存的文字
# --------------------------------------------------
records = [
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

# --------------------------------------------------
# 3. 寫入文字
# --------------------------------------------------
index.upsert_records(
    namespace=namespace,
    records=records
)

print("資料已寫入 Pinecone。")

# Pinecone 採 eventual consistency，
# 寫入後可能需要幾秒才可以搜尋
time.sleep(5)

# --------------------------------------------------
# 4. 查看 Index 統計資料
# --------------------------------------------------
stats = index.describe_index_stats()
print("\nIndex 統計：")
print(stats)

# --------------------------------------------------
# 5. 語意搜尋
# --------------------------------------------------
question = "什麼資料庫適合用來建立 RAG？"

results = index.search(
    namespace=namespace,
    query={
        "top_k": 3,
        "inputs": {
            "text": question
        }
    },
    fields=[
        "chunk_text",
        "category",
        "source"
    ]
)

# --------------------------------------------------
# 6. 顯示搜尋結果
# --------------------------------------------------
"""
print(f"\n問題：{question}")
print("=" * 60)

for hit in results["result"]["hits"]:
    print(f"ID：{hit['_id']}")
    print(f"分數：{hit['_score']}")
    print(f"內容：{hit['fields']['chunk_text']}")
    print(f"分類：{hit['fields']['category']}")
    print(f"來源：{hit['fields']['source']}")
    print("-" * 60)
"""
# 檢查 <class 'pinecone.models.vectors.search.SearchRecordsResponse'> 物件資訊：

# 1. 取得 hits 列表
hits = results.result.hits

# 2. 遍歷每一個搜尋結果 (Hit 物件)
print(f"\n問題：{question}")
print("=" * 60)

for hit in hits:
    # hit.id     : 記錄的唯一標記 (ID)
    # hit.score  : 相似度分數 (Similarity Score)
    # hit.fields : 包含文字或其它 metadata 的字典 (Dict)

    print(f"ID：{hit.id}")
    print(f"分數：{hit.score}")
    print(f"內容：{hit.fields.get('chunk_text')}")
    print(f"分類：{hit.fields.get('category')}")
    print(f"來源：{hit.fields.get('source')}")
    print("-" * 60)
</code>
```
## Prompt 2. 依據上述輸出結果建立 Python Flask 網站。
```markdown
依據<code>編寫一個Python Flask Web Application，規格如<spec>所述。
<spec>
  1. 建立向量資料庫的功能：
     - 可載入預設 data.json 資料。
     - 或是由使用者開啟檔案載入，寫入向量資料庫前，預先檢查格式是否正確。
  2. 查詢向量資料庫的功能：
     - 使用者輸入問題界面。
     - 查尋問題結果。
  3. 呈現查尋問題結果的頁面是動態頁面。
  4. 前端不使用CSS，也不使用Javascript。
</spec>
<code>
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
</code>
```
