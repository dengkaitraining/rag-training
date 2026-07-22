import json
from pathlib import Path
from flask import Flask, render_template, request
from pinecone_store import PineconeVectorStore

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_JSON_PATH = BASE_DIR / "data.json"

# 初始化 Pinecone 服務
vector_store = PineconeVectorStore()


@app.route("/")
def index():
    """首頁"""
    return render_template("index.html")


@app.route("/build", methods=["POST"])
def build_db():
    """建立/更新向量資料庫路由"""
    source_type = request.form.get("source_type")
    message = ""
    error = ""
    stats = None

    try:
        if source_type == "default":
            # 1. 載入預設 data.json
            count, stats = vector_store.build_vector_database(DEFAULT_JSON_PATH)
            message = f"成功從預設 data.json 載入並寫入 {count} 筆資料！"

        elif source_type == "upload":
            # 2. 上傳自訂 JSON 檔案
            file = request.files.get("json_file")
            if not file or file.filename == "":
                raise ValueError("請選擇要上傳的 JSON 檔案！")

            if not file.filename.endswith(".json"):
                raise ValueError("上傳檔案格式必須為 .json")

            # 嘗試解析 JSON
            try:
                content = file.read().decode("utf-8")
                records = json.loads(content)
            except Exception as e:
                raise ValueError(f"JSON 檔案解析失敗，請確認 JSON 格式是否合法。細節: {str(e)}")

            # 驗證與寫入
            count, stats = vector_store.build_vector_database_from_records(records)
            message = f"成功從上傳檔案 {file.filename} 寫入 {count} 筆資料！"

    except Exception as e:
        error = f"寫入向量資料庫失敗：{str(e)}"

    return render_template("index.html", build_message=message, build_error=error, stats=stats)


@app.route("/search", methods=["POST"])
def search_db():
    """查詢向量資料庫路由"""
    query = request.form.get("query", "").strip()
    top_k_str = request.form.get("top_k", "3")
    
    try:
        top_k = int(top_k_str)
    except ValueError:
        top_k = 3

    if not query:
        return render_template("index.html", search_error="請輸入搜尋問題！")

    try:
        results = vector_store.search_vector_database(query=query, top_k=top_k)
        return render_template(
            "index.html",
            query=query,
            top_k=top_k,
            results=results,
            searched=True
        )
    except Exception as e:
        return render_template("index.html", search_error=f"搜尋發生錯誤：{str(e)}")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)