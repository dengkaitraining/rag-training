### 組態設定(Configuration Setting)，將程式會用到的環境變數或常數設定在一個file，程式執行後在一開始就讀入組態值。
 - ```.env```  
 - ```*.conf```
 - ```*.md```
 - ```*.yaml```
### ```.env``` 是 ```Python``` 程式常用的
```ini
PINECONE_API_KEY=...
```
### RAG 的DB一般會是 local 的，Vector DB 也是。LLM 也會建置在Local，local server 最好要有GPU 或 TPU。
 - Vector DB  local 常用  Chrome DB, cpu-only
### pinecone 是線上的 Vector DB，要有 API Key 
```ini
PINECONE_API_KEY=.pcsk_6dVpfr_...
```
```python
# 建立 Pinecone Client，相當於在程式這一端的代理物件
pc = Pinecone(api_key=api_key)
```
### Data Center 就是算力中心 (包含Data Storage)
### 向量資料庫可以做到跨語言的語意檢索。
```python
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
    },
    {
        "_id": "doc-006",
        "chunk_text": "Netflix 是  Time Killer",
        "category": "Hpbby",
        "source": "DOC-123-tyyty"
    },
    {
        "_id": "doc-007",
        "chunk_text": "A blockchain is a distributed ledger with growing lists of records (blocks) that are securely linked together via cryptographic hashes.[1][2][3][4] Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data (generally represented as a Merkle tree, where data nodes are represented by leaves). Since each block contains information about the previous block, they effectively form a chain (viz. linked list data structure), with each additional block linking to the ones before it. Consequently, blockchain transactions are resistant to alteration because, once recorded, the data in any given block cannot be changed retroactively without altering all subsequent blocks and obtaining network consensus to accept these changes.",
        "category": "Hpbby",
        "source": "DOC-123-tyyty"
    },
     {
        "_id": "doc-008",
        "chunk_text": "MAGA就是讓美國再度偉大",
        "category": "politics",
        "source": "http://www.maga.gov.tw"
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

# ----- 至此  Vector DB完成 ----
#
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
question = "什麼是區塊鏈?"

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
print(f"\n問題：{question}")
print("=" * 60)

for hit in results["result"]["hits"]:
    print(f"ID：{hit['id']}")
    print(f"分數：{hit['score']}")
    print(f"內容：{hit['fields']['chunk_text']}")
    print(f"分類：{hit['fields']['category']}")
    print(f"來源：{hit['fields']['source']}")
    print("-" * 60)
```
