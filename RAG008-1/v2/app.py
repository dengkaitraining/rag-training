from pathlib import Path
from flask import Flask, render_template, request
from pinecone_store import PineconeVectorStore
from rag_service import RAGService

# 設定是否在 Console 印出詳細日誌訊息 (True: 開啟, False: 關閉)
CONSOLE_FLAG = True

# 取得根目錄路徑
BASE_DIR = Path(__file__).resolve().parent

# 初始化 Flask 應用程式
app = Flask(__name__)

if CONSOLE_FLAG:
    print("==================================================")
    print(" 啟動 Flask RAG Web Application ...")
    print("==================================================")

# 初始化 1: 實例化 Pinecone 向量資料庫，並傳入 CONSOLE_FLAG 控制開關
vector_store = PineconeVectorStore(console_flag=CONSOLE_FLAG)

# 啟動時自動檢查並載入預設資料庫 (knowledge.json)
data_json_path = BASE_DIR / "knowledge.json"
if data_json_path.exists():
    try:
        vector_store.build_vector_database(data_json_path)
    except Exception as e:
        if CONSOLE_FLAG:
            print(f"【系統警示】知識庫初始化或更新發生例外狀況：{e}")

# 初始化 2: 建立 RAG 服務，傳入 vector_store 實例與 CONSOLE_FLAG
rag_service = RAGService(vector_store, console_flag=CONSOLE_FLAG)


@app.route("/")
def index():
    """[GET] 渲染首頁提問輸入頁面"""
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    """
    [POST] 接收前端送出的問題，經由 RAGService 處理後，
    動態渲染包含搜尋結果的 output.html 頁面。
    """
    user_prompt = request.form.get("user_prompt", "")
    outstr = rag_service.process_query(user_prompt)

    # 渲染動態結果頁面
    return render_template("output.html", user_prompt=user_prompt, result=outstr)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)