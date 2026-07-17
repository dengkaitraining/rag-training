### Google Gemini API - curl
```bash
   curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
    -H 'Content-Type: application/json' \
    -H 'X-goog-api-key: {API_KEY}' \
    -X POST \
    -d '{
      "contents": [
        {
             "parts": [
            {
              "text": "請描述 Taiwan 這個國家的特色"
            }
          ]
        }
      ]
    }'
```
### Local Ollama API - curl
```bash
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2:latest",
  "messages": [
    { "role": "system", "content": "請描述 Taiwan 這個國家的特色" }
  ]
}'
```

### ```Latge Language Model``` 在學習完 ```Knowledge``` 後知識就 ```frozen``` 了。
### ```LLM``` 不等於 ```ChatGPT```，後者有 ```RAG``` 元素
### ```RAG (Retrieval Augmented Generation)```
 - ```Retrieval``` 的來源是特定知識庫 ```(Specific Knowledge)```，```Retrieval``` 的根據是 ```user_prompt```。
 - 從 ```context``` 找出 ```user_prompt``` 的答案，如果找不到就說不知道。
### 實現 ```RAG``` 系統，通常會安裝 ```Open Source LLM```
 - TAIDE，```TAIDE LX-13B (學研用版本)``` 模型，基於 ```Llama2  Open Source``` 再 ```Model Finetune(模型微調)``` -> 具臺灣特色與繁體中文的可信任生成式AI對話引擎 ```(Trustworthy AI Dialogue Engine, TAIDE)```
### ```RAG``` 的 ```Retrieval``` 可以從
 - (1) ```File```
 - (2) 關聯式資料庫
 - (3) ```Vector Database``` (向量資料庫)
 - (4) 其他資訊系統，例如 ```ERP```
 - (5) 第三方 ```API```
 - (6) 網路爬蟲

### ```User``` 的 ```user_prompt``` 是自然語言 ```(Natural Language)```
 - 收到 ```User_Prompt``` 到知識庫檢索出 ```context```，稱為 ```Retrieval Algorithm``` ，會因知識庫結構與特性不同而不同。

### 假設有一個知識庫是 {關鍵字, 描述}的結構，儲存在純文字檔 ```knowledge.txt``` 。描述是以"與"包含起來，儲存內容舉例如下：
```bash
# knowledge.txt
AI, "Artificial Intelligent, 主要分鑑別式AI與生成式AI"
IoT,"Internet of Things, 全面感知、數據處理、決策控制"
AI, "資料探勘有時也被稱為AI"
IoT,"各類感測器是蒐集數據的IoT終端裝置"
AI, "基因演算法這一類的最佳解搜尋也被稱為AI"
```
### 以此Knowledge為例，檢索演算法的執行步驟如下：
 1. 要從 ```User_Prompt``` 抽出關鍵字
 - Prompt：
```txt
編寫一個Python 函式，給定 User_Prompt，函式會比對 User_Prompt是否有{AI, IoT, Blockchain}等關鍵字，如果有就return，若沒有比對到就return 空list。使用Python re Module，也就是 Regualr Expression Module。關鍵字如果是英文vocabulary的一部分視為未比對到，如果出現在非英文詞後就當做比對到。
```
 2. 以關鍵字到 ```knowledge.txt``` 檢索出對應的內容
 - Prompt：
```txt
編寫一個 Python 函式，給定關鍵字可以到純文字檔 knowledge.txt 找出對應的內容。 
純文字檔 knowledge.txt 是 {關鍵字, 描述}的結構，每一行儲存一筆。每一個關鍵字可能有多筆。描述是以"與"包含起來，儲存內容舉例如下：
AI, "Artificial Intelligent, 主要分鑑別式AI與生成式AI"
IoT,"Internet of Things, 全面感知、數據處理、決策控制"
AI, "資料探勘有時也被稱為AI"
IoT,"各類感測器是蒐集數據的IoT終端裝置"
AI, "基因演算法這一類的最佳解搜尋也被稱為AI" 
```
 3. 如果有多筆，就組合成context


### 在 ```Python``` 裡，字串前面的 ```r``` 代表的是 ```Raw String```（原始字串）。
 - 它的主要作用是告訴 ```Python```：「請把字串裡的所有字元都當作普通的文字看待，不要對反斜線 ```（\）``` 進行跳脫 ```（Escape）``` 處理。」
 - **如果我們不加上** ```r```：
   當你想在正規表達式裡寫一個 ```\b```（單字邊界）時，```Python``` 會誤以為你要打一個特殊的跳脫字元```（Backspace）```。為了解決這個衝突，你必須打兩個反斜線 ```\\b```，讓 ```Python``` 知道你真的想要一個 ```\``` 再加上 ```b```。一旦規則變複雜，你的程式碼就會充滿 ```\\\\```，變得非常難以閱讀。
 - **如果加上了** ```r```：
   ```r'\b'``` 就會原封不動地傳給正規表達式的引擎，你寫什麼就是什麼，不需要一直重複打反斜線。
   ```pattern = r'(?<![a-zA-Z])(AI|IoT|Blockchain)(?![a-zA-Z])'```
   其實裡面 剛好沒有用到任何反斜線```（\）```。所以，就算您把 ```r``` 拿掉，寫成：
   ```pattern = '(?<![a-zA-Z])(AI|IoT|Blockchain)(?![a-zA-Z])'```
   程式也依然能完全正常運作。
 - 不過，在 ```Python``` 中只要是寫正規表達式```（Regular Expression）```，無論裡面有沒有反斜線，一律在最前面加上 ```r``` 已經是程式設計師的標準好習慣 ```（Best Practice）```。

### 如何將list的元素組成字串，中間用 。 隔開
 - ['```Artificial Intelligent```, 主要分鑑別式 ```AI``` 與生成式 ```AI```', '資料探勘有時也被稱為 ```AI```', '基因演算法這一類的最佳解搜尋也被稱為 ```AI```'] 是 ```ai_results``` = ```find_knowledge_by_keyword("AI")``` 的結果。
 - ```ai_results``` 是 ```list```
 - ```context="。".join(ai_results)```
