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
"""
print("=" * 60)
print("results type")
print("=" * 60)
print(type(results))
print("=" * 60)
print("results")
print("=" * 60)
print(results)
"""

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

