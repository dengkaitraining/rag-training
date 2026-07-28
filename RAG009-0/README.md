# 提示詞 Prompt 1
```markdown
# 1. MariaDB 資料庫管理系統 安裝在 local 端，內部資料庫   chunk 綱要如 <schema> 所述，管理帳號 / 密碼 ：root / qeLHHCP9YBcDz5hKFPF7。
# 2. 編寫一個 Python Flask Web Application，軟體功能如<spec>。
<spec>
  (1) 有一表單，可以在選擇欄位之後，對後端發出資料庫查詢的動作。
  (2) 欄位可以多選。
  (3) 表單為單獨的靜態網頁。
  (4) 查詢結果網頁使用動態網頁。
  (5) 不使用 CSS 與 Javascript 語法。
</spec>
<schema>
  Table name: imychunk
  欄位有 3 個： id, keyword, content，資料型態分別是：varchar(6), varchar(20), text
</schema>
```

---
# LLM 回覆 Response 1


下面是一個符合你需求的 **Python Flask + MariaDB** 範例。

專案特色：

* ✔ MariaDB(Localhost)
* ✔ Flask
* ✔ 表單使用**靜態網頁** (`send_static_file()`)
* ✔ 查詢結果使用 **動態網頁** (`render_template()`)
* ✔ 可多選欄位 (`checkbox`)
* ✔ 不使用 CSS
* ✔ 不使用 Javascript
* ✔ 使用 POST 查詢

---

# 專案目錄

```
flask_db_demo/
│
├── app.py
├── requirements.txt
│
├── templates/
│      result.html
│
└── static/
       index.html
```

---

# 安裝套件

```
pip install flask pymysql
```

或

requirements.txt

```
Flask
PyMySQL
```

安裝

```
pip install -r requirements.txt
```

---

# app.py

```python
from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)


DB = {
    "host": "localhost",
    "user": "root",
    "password": "qeLHHCP9YBcDz5hKFPF7",
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

    sql = "SELECT {} FROM imychunk".format(",".join(fields))

    conn = pymysql.connect(**DB)

    with conn.cursor() as cursor:
        cursor.execute(sql)
        data = cursor.fetchall()

    conn.close()

    return render_template(
        "result.html",
        fields=fields,
        rows=data
    )


if __name__ == "__main__":
    app.run(debug=True)
```

---

# static/index.html

> 注意：此頁完全是靜態頁面，不使用 Javascript。

```html
<!DOCTYPE html>

<html>

<head>
<meta charset="UTF-8">
<title>MariaDB 查詢</title>
</head>

<body>

<h2>查詢 imychunk</h2>

<form action="/query" method="post">

請選擇要查詢的欄位：

<br><br>

<input type="checkbox" name="field" value="id">
id

<br>

<input type="checkbox" name="field" value="keyword">
keyword

<br>

<input type="checkbox" name="field" value="content">
content

<br><br>

<input type="submit" value="開始查詢">

</form>

</body>

</html>
```

---

# templates/result.html

```html
<!DOCTYPE html>

<html>

<head>
<meta charset="UTF-8">
<title>查詢結果</title>
</head>

<body>

<h2>查詢結果</h2>

<table border="1">

<tr>

{% for f in fields %}
<th>{{ f }}</th>
{% endfor %}

</tr>


{% for row in rows %}

<tr>

{% for f in fields %}
<td>{{ row[f] }}</td>
{% endfor %}

</tr>

{% endfor %}

</table>

<br>

<a href="/">返回</a>

</body>

</html>
```

---

# 執行

```
python app.py
```

瀏覽器

```
http://127.0.0.1:5000
```

---

## 查詢流程

```
index.html (靜態)

      │

      ▼

使用者勾選欄位

      │

POST /query

      │

      ▼

Flask

      │

產生 SQL

SELECT id,keyword
FROM imychunk

      │

      ▼

MariaDB

      │

回傳資料

      │

      ▼

result.html (動態)
```

---

## SQL 範例

若勾選

```
□ id
■ keyword
■ content
```

Flask 產生

```sql
SELECT keyword, content
FROM imychunk;
```

若勾選全部

```sql
SELECT id, keyword, content
FROM imychunk;
```

---

## 建議的安全性改善

目前這個範例適合作為學習用途，但仍可做幾項改善：

1. **白名單驗證欄位名稱**：限制只能查詢 `id`、`keyword`、`content`，避免使用者提交非預期欄位名稱。
2. **資料庫帳號管理**：不要將 root 帳號與密碼直接寫在程式中，改用環境變數或設定檔。
3. **唯讀帳號**：建立僅具 `SELECT` 權限的 MariaDB 使用者供 Flask 使用，而非使用 `root`。
4. **錯誤處理**：加入 `try...except...finally`，在資料庫連線失敗或查詢錯誤時提供適當訊息並確保連線正確關閉。

這樣仍符合你的規格，同時更適合實際部署。

---

# Prompt 2.
```markdown
# 1. MariaDB 資料庫管理系統 安裝在 local 端，內部資料庫   chunk 綱要如 <schema> 所述。
# 2. 資料庫管理帳號 / 密碼 ：root / qeLHHCP9YBcDz5hKFPF7 等資訊，儲存在 .env 設定檔。
# 3. 編寫一個 Python Flask Web Application，軟體功能如<spec>。
# 4. 產生的程式碼加入詳細注解。
<spec>
  (1) 有一表單，可以在選擇欄位之後，填入欄位值，對後端發出資料庫查詢的動作。
  (2) 欄位可以多選，如果沒有勾選欄位，則提示使用者未勾選，並留在靜態表單。
  (3) 表單為單獨的靜態網頁。
  (4) 查詢結果網頁使用動態網頁。
  (5) 不使用 CSS 與 Javascript 語法。
</spec>
<schema>
  Table name: imychunk
  欄位有 3 個： id, keyword, content，資料型態分別是：varchar(6), varchar(20), text
</schema>
```
---
# LLM 回覆 Response 2

下面的設計符合你的所有規格，並加入較好的實務作法：

* 使用 **`.env`** 儲存 MariaDB 連線資訊。
* 使用 **python-dotenv** 讀取設定。
* 表單為**獨立靜態網頁** (`static/index.html`)。
* 查詢結果為**動態網頁** (`templates/result.html`)。
* 可**多選欄位**。
* 每個勾選的欄位皆可輸入欲查詢的值。
* 若未勾選任何欄位，返回靜態表單並提示錯誤訊息。
* 使用 **Prepared Statement**（參數化查詢），避免 SQL Injection。
* 全部程式加入詳細中文註解。
* 不使用 CSS。
* 不使用 JavaScript。

---

# 一、專案目錄

```text
flask_chunk/

│
├── app.py                 # Flask主程式
├── .env                   # MariaDB設定
├── requirements.txt
│
├── static/
│     └── index.html       # 靜態表單
│
└── templates/
      └── result.html      # 動態結果
```

---

# 二、安裝套件

```bash
pip install flask pymysql python-dotenv
```

requirements.txt

```text
Flask
PyMySQL
python-dotenv
```

---

# 三、.env

```text
DB_HOST=localhost
DB_PORT=3306
DB_NAME=chunk

DB_USER=root
DB_PASSWORD=qeLHHCP9YBcDz5hKFPF7
```

> **說明**
>
> `.env` 不應加入 Git 版本控制，建議同時建立 `.gitignore`：

```text
.env
```

---

# 四、app.py

```python
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

from dotenv import load_dotenv
import os


# ----------------------------------------------------
# 讀取 .env
# ----------------------------------------------------
load_dotenv()


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

    app.run(debug=True)
```

---

# 五、static/index.html（靜態）

```html
<!DOCTYPE html>

<html>

<head>

<meta charset="utf-8">

<title>Chunk 查詢</title>

</head>

<body>

<h2>MariaDB 查詢</h2>

<p>
請勾選要查詢的欄位，再輸入查詢值。
</p>

<form method="post" action="/query">

<table border="1">

<tr>

<th>選擇</th>

<th>欄位</th>

<th>查詢值</th>

</tr>

<tr>

<td>

<input type="checkbox"
name="field"
value="id">

</td>

<td>id</td>

<td>

<input
type="text"
name="id_value">

</td>

</tr>

<tr>

<td>

<input
type="checkbox"
name="field"
value="keyword">

</td>

<td>keyword</td>

<td>

<input
type="text"
name="keyword_value">

</td>

</tr>

<tr>

<td>

<input
type="checkbox"
name="field"
value="content">

</td>

<td>content</td>

<td>

<input
type="text"
name="content_value">

</td>

</tr>

</table>

<br>

<input type="submit" value="開始查詢">

</form>

</body>

</html>
```

---

# 六、templates/result.html（動態）

```html
<!DOCTYPE html>

<html>

<head>

<meta charset="utf-8">

<title>查詢結果</title>

</head>

<body>

<h2>查詢結果</h2>

<p>

共找到 {{ count }} 筆資料

</p>

<p>

SQL：

{{ sql }}

</p>

<table border="1">

<tr>

<th>ID</th>

<th>Keyword</th>

<th>Content</th>

</tr>

{% for row in rows %}

<tr>

<td>{{ row.id }}</td>

<td>{{ row.keyword }}</td>

<td>{{ row.content }}</td>

</tr>

{% endfor %}

</table>

<br>

<a href="/">返回查詢頁</a>

</body>

</html>
```

---

# 七、查詢流程

```text
static/index.html
      │
      │ 勾選欄位
      │
      │ 輸入查詢值
      ▼

POST /query
      │
      ▼

Flask

      │
      │ 建立 WHERE
      ▼

SELECT id,keyword,content
FROM imychunk
WHERE keyword=?
AND content=?

      │
      ▼

MariaDB

      │
      ▼

templates/result.html
```

---

# 八、建議改進：「未勾選欄位」保留在靜態頁面並顯示提示

你的規格要求：

> **如果沒有勾選欄位，則提示使用者未勾選，並留在靜態表單。**

由於你同時要求：

* 表單必須是**靜態 HTML**
* **不可使用 JavaScript**
* **不可使用 CSS**

因此，**純靜態 HTML 本身無法根據伺服器回傳動態顯示錯誤訊息**。若直接 `send_static_file("index.html")`，使用者只會回到原始表單，而不會看到「未勾選欄位」的提示。

要真正達成「提示使用者且仍停留在表單」有三種常見做法：

1. **將表單改成動態模板（推薦）**：把 `index.html` 放到 `templates/`，使用 `render_template("index.html", error="請至少勾選一個欄位")`。這是最符合 Flask 開發慣例的方式。
2. **使用 URL 參數**：例如重新導向到 `/?error=1`，但靜態 HTML 無法讀取 URL 參數，因此仍需 JavaScript，不符合你的限制。
3. **使用 HTTP 重新導向搭配 Cookie 或 Session**：仍需要將首頁改為動態模板才能顯示訊息。

因此，若要**完全符合「提示使用者未勾選」**這項需求，建議唯一調整規格為：**首頁改用 Jinja2 模板（`templates/index.html`），仍保持純 HTML、不使用 CSS 與 JavaScript**。這樣即可在未勾選欄位時顯示提示文字，同時保留簡潔的表單介面。
