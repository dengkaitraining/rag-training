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


## Prompt 3. 
```markdown
# 1. 完成將<code>依據 <spec> 建立與 python 物件導向的規範，封裝為 class。
# 2. 另外產生呼叫 class 測試的 CLI 建立搜尋的輸入界面。
<spec>
 1. API_KEY 等參數透過 .env 檔案儲存參數。
 2. 檔案讀取使用 from pathlib import Path 讀取絕對路徑。
</spec>
<code>
from flask import Flask, request, render_template
import os
import requests
import re
import markdown

def markdown_to_html(md_text: str) -> str:
    """
    將 Markdown 字串轉換成 HTML 字串。

    Parameters
    ----------
    md_text : str
        Markdown 格式的文字

    Returns
    -------
    str
        HTML 字串
    """
    html = markdown.markdown(
        md_text,
        extensions=[
            "extra",        # 支援表格、fenced code block 等擴充語法
            "codehilite",   # 程式碼語法高亮（需搭配 pygments）
            "toc"           # 產生目錄 ID
        ]
    )
    return html


def find_knowledge_by_keyword(keyword, file_path="knowledge.txt"):
    """
    從指定的知識庫檔案中，找出對應關鍵字的所有描述。
    
    :param keyword: 要搜尋的關鍵字 (例如: "AI", "IoT")
    :param file_path: 檔案路徑，預設為 "knowledge.txt"
    :return: 包含所有對應描述的 list，若未比對到或檔案不存在則回傳空 list []
    """
    results = []
    
    # 1. 安全檢查：確認檔案是否存在
    if not os.path.exists(file_path):
        print(f"提示：找不到檔案 {file_path}")
        return results
        
    # 2. 定義解析每行格式的正規表達式
    # ^\s*([^,]+?) : 從開頭匹配「非逗號」的字元作為關鍵字，並自動忽略前面的空白
    # \s*,\s* : 匹配關鍵字與雙引號之間的逗號，並忽略其前後的空白
    # "(.*?)"      : 匹配被雙引號 " 包含起來的描述內容（Group 2）
    # \s*$         : 確保結尾，並忽略後方的空白
    line_pattern = r'^\s*([^,]+?)\s*,\s*"(.*?)"\s*$'
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue  # 跳過空行
                
                # 使用 re.match 進行整行解析
                match = re.match(line_pattern, line)
                
                if match:
                    parsed_keyword = match.group(1)   # 萃取出的關鍵字
                    description = match.group(2)      # 萃取出的描述內容
                    
                    # 進行比對（此處採用「忽略大小寫」的比對，若要嚴格比對可改為 parsed_keyword == keyword）
                    if parsed_keyword.lower() == keyword.lower():
                        results.append(description)
                else:
                    # 格式不符時的提示（可選）
                    print(f"警告：第 {line_number} 行格式不符，已跳過：{line}")
                    
    except IOError as e:
        print(f"讀取檔案時發生錯誤: {e}")
        
    return results


def extract_tech_keywords(user_prompt):
    """
    比對 User_Prompt 是否包含 AI, IoT, Blockchain 等關鍵字。
    - 若為英文 vocabulary 的一部分（前後緊接英文字母）則視為未比對到。
    - 若出現在非英文詞（如中文、標點符號、空白）前後，則當作比對到。
    """
    
    # 定義正規表達式
    # (?<![a-zA-Z]) : 確保前面不是英文字母
    # (AI|IoT|Blockchain) : 比對的關鍵字群組
    # (?![a-zA-Z])  : 確保後面不是英文字母
    pattern = r'(?<![a-zA-Z])(AI|IoT|Blockchain|AR|VR)(?![a-zA-Z])'
    
    # 使用 re.findall 找出所有符合的字串
    # 加入 re.IGNORECASE 讓比對不區分大小寫
    matches = re.findall(pattern, user_prompt, flags=re.IGNORECASE)
    
    return matches

	
	

app = Flask(__name__)


@app.route("/")
def index():
    # 使用靜態網頁 index.html
    # 注意：這裡使用 app.send_static_file()
    return app.send_static_file("index.html")


@app.route("/process", methods=["POST"])
def process():
    # 從 <form> 接收 user_prompt 欄位
    user_prompt = request.form.get("user_prompt")
    tempstr=user_prompt
    #從user_prompt取出我們知識庫可以回答的關鍵字
    matches=extract_tech_keywords(user_prompt)
    if matches:
      searchStr=matches[0]
    else:
      return "<H1>你的問題太高深了，本仙人功力不足以回答。</H1><a href='/'>回提問頁</a>"
    print(searchStr)
    user_prompt ="<user_prompt>" + user_prompt + "</user_prompt>"
    
	#到  Knowledge 檢索出 context
    ai_results = find_knowledge_by_keyword(searchStr)
    context="。".join(ai_results)
    
    #context="Artificial Intelligent, 主要分鑑別式AI與生成式AI。資料探勘有時也被稱為AI。基因演算法這一類的最佳解搜尋也被稱為AI"
    context="<context>" + context + "</context>"
	
    #context="""<context>
	#AI Agent 時代 ─ 從工具走向自主協作，企業自動化正在被重新定義！
    #當大型語言模型（LLM）結合 Workflow、API 與企業系統，自動化不再只是流程優化，而是邁向具備情境理解與跨系統協作能力的 Agentic Automation 新階段。
	#IOT是Internet of Things，感測環境，蒐集數據，進行控制。
	#</context>
	#"""
    
    # 加上  Augmented 的 context 與 Specifier
    specifier="<specifier>從context找出user_prompt的答案，如果找不到就說不知道</specifier>"	
    system_prompt= user_prompt + context + specifier
    # 向 LLM API發出 Request，得到回應，送到 ouput.html呈現
    API_KEY = os.getenv("GEMINI_API_KEY")
    if not API_KEY:
      raise ValueError("找不到 GEMINI_API_KEY，請先設定環境變數")
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

    headers = {
      "Content-Type": "application/json",
      "X-goog-api-key": API_KEY
    }

    data = {
      "contents": [
          {
            "parts": [
                {
                    "text": system_prompt
                }
            ]
          }
       ]
    }

    # 這是向LLM API 發出POST, Request
    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    #print(response.json())
    result=response.json()
    #只取出 text 欄位(key)的內容(value)
    outstr=result['candidates'][0]['content']['parts'][0]['text']
    outstr=markdown_to_html(outstr)
    print(outstr)
    # 將user_prompt與result 傳給動態網頁 output.html再呈現給User
    return render_template("output.html", user_prompt=tempstr,result=outstr)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
</code>
```