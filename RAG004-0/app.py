from flask import Flask, request, render_template
import os, requests, re, json, markdown

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

def markdown_to_html(markdown_text):
    """將 Markdown 文字轉換為具備語法高亮擴充的 HTML"""
    return markdown.markdown(markdown_text, extensions=['extra', 'codehilite'])
    #return markdown.markdown(markdown_text)

def remove_xml_tags(xml_string):
    # 匹配以 < 开始，> 结束的任意字符
    clean_r = re.compile(r'<[^>]+>')
    return clean_r.sub('', xml_string)

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
    #user_prompt ="<user_prompt>" + user_prompt + "</user_prompt>"

	# 加上  Augmented 的 context 與 Specifier
    matches = find_knowledge_by_keyword(user_prompt, "knowledge.txt")
    if matches:
        user_prompt = '。'.join(matches)
    else:
        return f"<h1>無法回覆您提出的問題：『<font color=\"red\">{user_prompt}</font>』。</h1><br/><br/><a href=\"/\">回到表單頁面</a>"
    print(user_prompt)

    user_prompt ="<user_prompt>" + user_prompt + "</user_prompt>"

    raw_user_prompt = remove_xml_tags(user_prompt)

    context="""<context>
	  AI Agent 時代 ─ 從工具走向自主協作，企業自動化正在被重新定義！
      當大型語言模型（LLM）結合 Workflow、API 與企業系統，自動化不再只是流程優化，而是邁向具備情境理解與跨系統協作能力的 Agentic Automation 新階段。
	  IOT是Internet of Things，感測環境，蒐集數據，進行控制。
      人工智慧（Artificial Intelligence, AI）與物聯網（Internet of Things, IoT）是現今智慧科技發展的兩大核心技術，兩者相互結合，正逐步改變人們的生活與產業運作模式。
      人工智慧主要可分為**鑑別式 AI（Discriminative AI）**與**生成式 AI（Generative AI）**兩大類。鑑別式 AI 擅長分析資料、辨識影像、分類與預測，例如人臉辨識、垃圾郵件過濾等；生成式 AI 則能根據既有資料產生新的內容，例如文字、圖片、程式碼與音樂，是近年來發展最受矚目的 AI 技術。此外，在較廣義的定義下，**資料探勘（Data Mining）**利用大量資料分析找出規律與知識，也常被視為人工智慧的應用之一；而**基因演算法（Genetic Algorithm）**則透過模擬生物演化機制，尋找複雜問題的最佳解，因此也屬於人工智慧的重要方法之一。
      物聯網則是透過網際網路將各種設備彼此連接，形成智慧化的資訊網路，其核心概念包含**全面感知、數據處理與決策控制**。首先，透過溫度、濕度、光線、壓力、GPS、攝影機等各類感測器，蒐集環境與設備的即時資訊，這些感測器便是物聯網最重要的終端裝置。接著，系統將蒐集到的大量數據傳送至雲端或邊緣運算平台進行分析，最後依據分析結果自動做出控制與決策，例如智慧家庭自動調節空調、智慧工廠監控設備運作，以及智慧城市管理交通號誌等。
      當 AI 與 IoT 相互結合時，便形成了智慧化應用的重要基礎。IoT 負責持續蒐集大量即時資料，而 AI 則利用這些資料進行分析、學習與預測，進一步協助系統做出最佳決策，使設備具備自主判斷與自動控制的能力。未來，隨著生成式 AI、資料分析技術及物聯網持續發展，智慧醫療、智慧製造、智慧交通與智慧城市等領域都將獲得更廣泛的應用，為人類帶來更便利、更高效率的生活與工作環境。
	  </context>
	"""
    specifier="<specifier>從context找出user_prompt的答案，如果找不到就說不知道</specifier>"	
    user_prompt= user_prompt + context + specifier
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
                    "text": user_prompt
                }
            ]
          }
       ]
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    #print(response.json())
    #result=response.json()

    # 方法一
    #result=((response.json())['candidates'][0]['content']['parts'][0]['text'])

    # 方法二
    result=(
        (response.json()).get('candidates', [{}])[0]
                         .get('content', {})
                         .get('parts', [{}])[0]
                         .get('text', '找不到內容')
    )

    # markdown 轉 html
    result = markdown_to_html(result)

    # 將收到的 user_prompt 傳給動態網頁 output.html
    return render_template("output.html", user_prompt=raw_user_prompt,result=result)


if __name__ == "__main__":

        # 模擬建立測試用的 knowledge.txt 檔案
    #sample_content = """AI, "Artificial Intelligent, 主要分鑑別式AI與生成式AI"
#IoT,"Internet of Things, 全面感知、數據處理、決策控制"
#AI, "資料探勘有時也被稱為AI"
#IoT,"各類感測器是蒐集數據的IoT終端裝置"
#AI, "基因演算法這一類的最佳解搜尋也被稱為AI"
#"""
    
#    with open("knowledge.txt", "w", encoding="utf-8") as f:
#        f.write(sample_content)
        
#    print("--- 測試檔案 knowledge.txt 建立成功 ---\n")

    app.run(debug=True, host="0.0.0.0")