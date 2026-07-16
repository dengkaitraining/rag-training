from flask import Flask, request, render_template
import os
import requests

import re

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

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    #print(response.json())
    result=response.json()
    # 將收到的 user_prompt 傳給動態網頁 output.html
    return render_template("output.html", user_prompt=user_prompt,result=result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")