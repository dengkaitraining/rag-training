"""
Flask + MariaDB 查詢範例

功能：

1. 首頁使用靜態 HTML
2. 可多選查詢欄位
3. 每個欄位皆可輸入查詢值
4. 查詢結果使用動態HTML
5. 使用 .env 儲存資料庫資訊
6. 使用 Prepared Statement 防止 SQL Injection
"""

from flask import Flask
from flask import request
from flask import render_template

import pymysql

from pathlib import Path
from dotenv import load_dotenv
import os

# 取得根目錄路徑
BASE_DIR = Path(__file__).resolve().parent

# ----------------------------------------------------
# 讀取 .env
# ----------------------------------------------------
load_dotenv(BASE_DIR / ".env")


app = Flask(__name__)


# ----------------------------------------------------
# 建立資料庫連線
# ----------------------------------------------------
def get_connection():

    return pymysql.connect(

        host=os.getenv("DB_HOST"),

        port=int(os.getenv("DB_PORT")),

        user=os.getenv("DB_USER"),

        password=os.getenv("DB_PASSWORD"),

        database=os.getenv("DB_NAME"),

        charset="utf8mb4",

        cursorclass=pymysql.cursors.DictCursor
    )


# ----------------------------------------------------
# 首頁
#
# 使用靜態HTML
# ----------------------------------------------------
@app.route("/")
def index():

    return app.send_static_file("index.html")


# ----------------------------------------------------
# 查詢
# ----------------------------------------------------
@app.route("/query", methods=["POST"])
def query():

    # 取得所有勾選欄位
    fields = request.form.getlist("field")

    # ------------------------------------------------
    # 若沒有勾選任何欄位
    # ------------------------------------------------
    if len(fields) == 0:

        return app.send_static_file("index.html")


    # ------------------------------------------------
    # 建立 WHERE 條件
    # ------------------------------------------------
    conditions = []

    values = []


    # 白名單
    allow = ["id", "keyword", "content"]


    for field in fields:

        if field not in allow:
            continue

        value = request.form.get(field + "_value", "").strip()

        # 有輸入才加入查詢條件
        if value != "":

            conditions.append(f"{field}=%s")

            values.append(value)


    sql = "SELECT id, keyword, content FROM imychunk"


    if len(conditions) > 0:

        sql += " WHERE "

        sql += " AND ".join(conditions)


    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(sql, values)

    rows = cursor.fetchall()

    cursor.close()

    conn.close()


    return render_template(

        "result.html",

        sql=sql,

        rows=rows,

        count=len(rows)

    )


if __name__ == "__main__":

    app.run(host='0.0.0.0',debug=True,port=60000)