from flask import Flask, request, render_template
import os
import requests
import re
from pathlib import Path

def extract_tech_keywords(user_prompt: str) -> list:
    """
    檢查 user_prompt 中是否包含 AI, IoT, Blockchain 等關鍵字。
    - 關鍵字如果是英文單字的一部分（如 paint 裡的 ai），視為未比對到。
    - 關鍵字如果出現在非英文詞後（如 '中文AI'、'標點!AI'、'空格 AI'），視為比對到。
    """
    keywords = ["AI", "IoT", "Blockchain"]
    
    # 用 | 將關鍵字結合
    joined_keywords = '|'.join(keywords)
    
    # (?<![a-zA-Z]) 代表左邊不能是英文字母
    # (?![a-zA-Z])  代表右邊不能是英文字母
    pattern = rf'(?<![a-zA-Z])({joined_keywords})(?![a-zA-Z])'
    
    # 進行不區分大小寫的比對
    matches = re.findall(pattern, user_prompt, re.IGNORECASE)
    
    return matches

def search_knowledge_by_keyword(keyword: str, file_path: str = Path(__file__).parent / "knowledge.txt") -> list:
    """
    從指定的知識庫檔案中，搜尋與給定關鍵字相符的所有描述。
    
    :param keyword: 欲搜尋的關鍵字（例如 'AI' 或 'IoT'）
    :param file_path: 知識庫檔案路徑，預設為 'knowledge.txt'
    :return: 包含所有對應描述內容的 list。若無比對到，則回傳空 list []。
    """
    # 檢查檔案是否存在，若不存在則回傳空 list
    if not os.path.exists(file_path):
        print(f"錯誤：找不到檔案 {file_path}")
        return []
        
    results = []
    
    # 正規表示式解析規則：
    # ^\s*([^,\s]+)  : 匹配行首可能存在的空白，並抓取不包含逗號與空白的「關鍵字」
    # \s*,\s*        : 匹配關鍵字與雙引號之間的逗號，並忽略前後多餘空白
    # "(.*)"\s*$     : 匹配被雙引號 " " 包裹起來的「描述內容」，並抓取引號內的所有字元
    pattern = re.compile(r'^\s*([^,\s]+)\s*,\s*"(.*)"\s*$')
    
    # 讀取檔案進行比對
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 去除行尾換行符號
            line = line.strip()
            if not line:
                continue
                
            # 使用 re 比對該行結構
            match = pattern.match(line)
            if match:
                file_keyword, description = match.groups()
                
                # 進行不區分大小寫的關鍵字比對 (若需嚴格區分大小寫，可改為: if file_keyword == keyword)
                if file_keyword.strip().lower() == keyword.strip().lower():
                    results.append(description)
                    
    return results

app = Flask(__name__)


@app.route("/")
def index():
    # 使用靜態網頁 index.html
    # 注意：這裡使用 app.send_static_file()
    return app.send_static_file("index.html")


@app.route("/process", methods=["POST"])
def process():
    # 2026-07-13 從 <form> 接收 user_prompt 欄位
    user_prompt = request.form.get("user_prompt")
    #user_prompt = "<user_prompt>" + user_prompt + "</user_prompt>"

    # 2026-07-14 Augment 的 conrtext 與 specifier
    #matches = extract_tech_keywords(user_prompt)
    matches = search_knowledge_by_keyword(user_prompt)
    if matches:
        user_prompt = ', '.join(matches)
    else:
        return f"<h1>無法回覆您提出的問題。{matches}</h1>"
    print(user_prompt)

    user_prompt = "<user_prompt>" + user_prompt + "</user_prompt>"
    context = """<context>
      AI Agent 時代 - 從工具走向自主協作，企業自動化正在被重新定義！
      當大型語言婆型（LLM）結合 Workflow、API 與企業系統，自動化不再只是流程優化，而是邁向具備具備情境理解與系統協作能力的 Agentic Automation。
      IOT是Internet of Things，感測環境，蒐集數據，進行控制。
    </context>"""

    specifier = """<specifier>
      從 context 找出 user_prompt 的答案，如果找不到請回答不知道。
    </specifier>"""

    user_prompt = user_prompt + context + specifier

    # 2026-07-13 向 LLM API發出 Request，得到回應，送到 ouput.html呈現
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
                    "text": user_prompt
                }
            ]
          }
       ]
    }


    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())
    result=response.json()

    # 2026-07-14 將收到的 user_prompt 傳給動態網頁 output.html
    return render_template("output.html", user_prompt=user_prompt,result=result)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)