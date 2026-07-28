from flask import Flask, request, render_template
import pymysql
from dotenv import load_dotenv
import os

load_dotenv(".env")

app = Flask(__name__)


DB = {
    "host": "localhost",
    "user": os.getenv("db_user"),
    "password": os.getenv("db_passwd"),
    "database": "chunk",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor
}


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/query", methods=["POST"])
def query():

    fields = request.form.getlist("field")

    if len(fields) == 0:
        return "請至少選擇一個欄位"

    # 建立 SQL 指令
    # SELECT content FROM imychunk
    # SELECT id,content FROM imychunk
    # SELECT id,keyword,content FROM imychunk
    sql = "SELECT {} FROM imychunk".format(",".join(fields))

    conn = pymysql.connect(**DB)

    with conn.cursor() as cursor:
        cursor.execute(sql)         # SQL 執行
        data = cursor.fetchall()    # 

    conn.close()

    return render_template(
        "result.html",
        fields=fields,
        rows=data
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)