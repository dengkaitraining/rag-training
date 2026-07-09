### HTML hyperlink ```<a>``` 會超連結到一個資源(resource),實際上就是發出Request,要求Response所要求資源回到 Browser。
 - 所謂 ```resource``` 可以是 ```html``` 檔、```jpg``` 檔、...或任何其他檔;
 - ```resource``` 也可以是 ```Python Flask``` 的一個 ```route``` , ```@app.route("/dynamic")```,會 ```invoke``` (觸發) 該 route底下的函式執
行。
 - ```<a href="/dynamic">中獎了</a> <p>``` 使用者 ```click``` 之後就會觸發 @app.route("/dynamic") 的函式執行
```python
@app.route("/dynamic")
def dynamic():
# 隨機生成一個0到50的數字,儲存到 dog 變數
dog = random.randint(0, 50)
print(dog)
return render_template("lucky.html",num = dog)
```
 - ```target="_new"``` 會讓 ```response``` 回來的內容,呈現(渲染,render)在名為 "_new"的窗格,若 _new不存在就開啟一個新的。```<a href="/dynamic" target="_new">中獎了</a> <p>```

### API Service
 - Application Programming Interface (API)是Web Service提供服務的窗口,呼叫API Service通常回傳的是 JSON格式的資料;通常我們會在自己的 Application, 寫代碼(Programming)呼叫第三方的API服務,但需要遵照它的規範(Interface)。
 - 目前最常使用的第三方API服務是LLM API
 - 我們也可以讓自己的網站提供API服務,例如只要給 /api/weather 我們網站就回傳高雄的溫度(temperature)與天氣狀況(condition)。
```python
@app.route("/api/weather")
def weather():
return
jsonify({"city":"Kaoshiung","temperature":30,"condition":"Sunny"})
```
### HTTP 協定有2個角色:http Server 與 http Client
 - Browser只是 HTTP Client的一種
 - curl.exe 也是一種 HTTP Client ,它是 CLI (Command Line Interface),命令列的操作介面
 - PowerShell CLI 與 cmd CLI ,前者是Developer 在用,cmd是給一般user
```powershell
PS C:\Users\weichih> curl.exe http://127.0.0.1:5000/api/weather
{
"city": "Kaoshiung",
"condition": "Sunny",
"temperature": 30
}
```
### LLM API Service 以 Google Gemeni API 為例
 - 1. 到 Google AI Studio 取得 API Key ,
```sh
Google AI API Key
```
 - 2. 使用 curl.exe 發出 Request,
```sh
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
-H 'Content-Type: application/json' \
-H 'X-goog-api-key: GOOGLE-API-KEY' \
-X POST \
-d '{
        "contents": [
            {
                "parts": [
                    {
                        "text": "Explain how AI works in a few words"
                    }
                ]
            }
        ]
    }'
```
Response : 
```sh
台灣(Taiwan)是一個位於東亞、太平洋西側的島嶼國家。儘管國
土面積不大(約3.6萬平方公里),但台灣在經濟、科技、民主政
治、文化和自然景觀等方面,都展現出極為獨特且強大的影響力。
\n\n以下是台灣這個國家的主要特點:\n\n### 1. 全球科技與半導
體重鎮(矽盾)\n* **半導體王國:** 台灣是全球高科技產業的核
心。以台積電(TSMC)為首的台灣半導體產業,製造了全球絕大
多數的最先進晶片。這使得台灣在全球供應鏈中具有無可替代的戰
略地位,被媒體稱為保護台灣安全的「矽盾」。\n* **資訊與通訊
產業(ICT):** 台灣在筆記型電腦、伺服器、電子配件等硬體製
造上,同樣居於全球領先地位。\n\n### 2. 亞洲民主與人權的燈塔
\n* **高度民主化:** 台灣經歷了和平的民主轉型,如今是亞洲最
民主、最自由的國家之一。在各項國際民主、新聞自由和經濟自由
度指數中,台灣常年名列亞洲前茅。\n* **進步的社會價值:** 台
灣在人權和多元包容性上非常 先進。2019年,台灣成為**亞洲第
一個同性婚姻合法化**的國家,展現了對多元性別(LGBTQ+)的
高度包容。\n* **社會安全:** 台灣是全球治安最好 的國家之一,
犯罪率極低,即便是深夜出行也十分安全。\n\n### 3. 世界級的醫
療與社會福利\n* **全民健康保險(NHI):** 台灣的「全民健保」
制 度聞名全球,以低成本、高覆蓋率、高效率和優質的醫療服務
著稱,常被許多國家視為醫療改革的典範。\n\n### 4. 多元融合的
文化與歷史底蘊\n台灣 歷史經歷了多個時期(原住民、荷西時期、
明鄭時期、清領時期、日本統治時期以及中華民國政府遷台),形
成了極具包容性的多元文化:\n* **南島語族的發源地:** 台灣原
住民族(現有16族得到官方認定)擁有豐富的語言與文化,許多語
言學研究指出台灣是南島語族的祖居地。\n* **中華傳統文化 的保
存者:** 台灣完整地保存了繁體中文(正體字),並將傳統的民俗
信仰(如媽祖遶境、廟會文化)與現代生活完美融合。\n* **日本
與西方文化的 薰陶:** 日本統治時期留下的建築、飲食習慣,以
及戰後西方流行文化的引進,共同形塑了台灣當代獨特的「哈
日」、「生活美學」與咖啡廳文化。\n\n### 5. 美食天堂\n台灣的
飲食文化是吸引全球遊客的一大亮點:\n* **夜市文化:** 台灣的
夜市(如士林夜市、逢甲夜市等)是庶民美食的集中地, 展現了
活力四射的夜生活。\n* **代表性美食:** 珍珠奶茶(已風靡全

球)、牛肉麵、小籠包(如鼎泰豐)、滷肉飯、芒果冰和各式街頭
小吃。\n\n### 6. 壯麗多樣的自然景觀\n雖然是座島嶼,但台灣的
地形極具多樣性,幾小時內就能從海平線上升到海拔三千公尺以
上:\n* **高山林立:** 台灣是世 界上高山密度最高的島嶼之一,
海拔3,000公尺以上的高山多達268座。其中主峰「玉山」(海拔
3,952公尺)是東北亞第一高峰。\n* **自然奇景:** 擁有世界級的
太魯閣大理石峽谷、阿里山的日出與神木、日月潭的湖光山色,以
及四面環海的蔚藍海岸(如墾丁、東海岸)。\n\n### 7. 溫暖、友
善的人 情味\n「台灣最美的風景是人」這句話常被外國旅客提起。
台灣人普遍對外國人極為友善、樂於助人,社會展現出高度的禮貌
與互助精神(例如在捷運上主動讓座、拾金不昧等)。\n\n### 總
結\n台灣是一個**「小而強大、溫暖且堅韌」**的國家。儘管在國
際外交上面臨特殊的地緣政治挑戰,但台灣憑藉著頂尖的科技實
力、傲人的民主成就、豐富的文化與無比的韌性,在世界上站穩了
腳步,成為不容忽視的重要存在。
```

### 將 Powershell 顯示符號時,採用 UTF8 去解讀, CLI下
```powershell
$OutputEncoding = [System.Text.Encoding]::UTF8
# [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
```
### LLM 很強大,但是會有hallicination (幻文,幻覺),對企業來說,LLM要落地應用,就必須要能回答企業的相關問題。
 - Prompt 時,給內容,並限定它只能從給的內容找答案,如果找不到就說不知道。
 - Prompt = User_Prompt + ```<context>``` + ```<specifier>```
 - ```<context>``` 若來自企業特定知識庫,那麼就不會亂回答了。

### RAG (Retrieval Augmented Generation)
 - 生成文本前(Generation),參考附加的內容(Augmented),附加的內容來自檢索的結果(Retrieval)。檢索的資料來源可以是網站、資料庫、檔案、會其它資訊系統。

## RAG 系統Prompt的結構

```xml
<user_prompt>如何美白?</user_prompt>
<context>生成文本前(Generation),參考附加的內容
(Augmented),附加的內容來自檢索的結果(Retrieval)。檢索的
資料來源可以是網站、資料庫、檔案、會其它資訊系統。
</context>
<specifier>根據context回答user_prompt,如果找不到答案就說
不知道,不要自己衍伸。
</specifier>
```
 - context就是檢索來的;檢索的步驟是開發 RAG 系統的人要自己 Coding
### JSON格式
 - 1. key-value pairs
 - 2. 使用 { 與 } 將一筆資料紀錄(record)包含起來
 - 3. 一筆資料紀錄會有多個 key-value pair,每一個使用 , 隔開。
 - 4. 使用 [與] 將多筆資料紀錄包含起來 [{k:v,k:v,k:v},{k:v,k:v,k:v},{k:v,k:v,k:v}]
 - 5. value 也可以是{},或者[]

### PowerShell 的command
```powershell
curl.exe "https://generativelanguage.googleapis.com/v1beta/models/gemini-
flash-latest:generateContent" `

-H 'Content-Type: application/json' `
-H 'X-goog-api-key: GOOGLE-API-KEY' `
-X POST `
-d '@mydata.json'
{
"contents": [
{
"parts": [
{

"text": "<user_prompt>如何美白?</user_prompt>
<context>生成文本前(Generation),參考附加的內容
(Augmented),附加的內容來自檢索的結果(Retrieval)。檢索的
資料來源可以是網站、資料庫、檔案、會其它資訊系統。
</context>
<specifier>根據context回答user_prompt,如果找不到答案就說
不知道,不要自己衍伸。
<specifier>"
}
]
}
]
}

-- response
{
"candidates": [
{
"content": {
"parts": [
{
"text": "不知道",
"thoughtSignature": "EuIOCt8wnuepru"
}
],
"role": "model"
},
"finishReason": "STOP",

"index": 0
}
],
"usageMetadata": {
"promptTokenCount": 86,
"candidatesTokenCount": 1,
"totalTokenCount": 537,
"promptTokensDetails": [
{
"modality": "TEXT",
"tokenCount": 86
}
],
"thoughtsTokenCount": 450,
"serviceTier": "standard"
},
"modelVersion": "gemini-3.5-flash",
"responseId": "m91NaoKoNe2_vr0P3vX0iAY"
}
```

### Markdown format
```markdown
### 國立高雄科技大學 電通系 徐偉智教授

**徐偉智教授**任教於國立高雄科技大學(NKUST)電腦與通訊工
程系。他擁有深厚的學術與實務背景,研究與授課領域橫跨資通訊
技術、區塊鏈、軟體工程與人工智慧應用。

#### 🎓 學經歷

* **學歷**:國立台灣大學電機工程學士、國立台灣大學電機工程研
究所博士。
* **重要經歷**:
* 國立高雄第一科技大學(高科大前身之一)電通系 第 7 任系主任
* 國立高雄第一科技大學 圖資館館長
* 美國普渡大學 訪問學者
* 交通部電信研究所 副研究員
* 海軍通信電子學校 專業科目教官
```

### 要開發一個RAG系統讓User可以查公司的產品資訊
 - User 要有一個輸入介面,可以輸入 User_Prompt
 - 後端收到 User_Prompt後去檢索產品知識庫,得到Product Knowledge,也就是 Context
 - User_Prompt + Context + Specifier 向LLM API 發出Request
 - LLM API Response 回來的JSON 資料,要進行 Parsing,取出 text 欄位的資料內容
 - 資料內容 是Markdown,轉換成 HTML後,response 給 User

### HTML的 ```<form>``` 可以呈現輸入欄位,使用者填了之後,可以送到後端處理。
### Prompting
```xml
編寫一個Python Flask 範例,展示<form>送出資料到後端處理的過
程,規格如<spec>所述。
<spec>
1. <form>只有一個 user_prompt輸入欄位。
2. <form>的資料以POST送到 route /process 處理
3. 處理的動作是將收到的 User_prompt Echo 回 Browser,以動態
網頁的方式。也就是有一個動態網頁 output.html,可以接收
User_Prompt。output.html不使用CSS。
4. <form>網頁使用靜態網頁的方式,send_static_file()。不使用
CSS語法。
</spec>
```
 - ```<form>``` 可以設定,資料送到哪裡處理
```html
<form action="/process" method="POST">
<label for="user_prompt">請輸入 User Prompt:</label>
<input type="text" id="user_prompt" name="user_prompt">

<button type="submit">送出</button>
</form>
```
 - app.py 內
```python
@app.route("/process", methods=["POST"])
def process():
# 從 <form> 接收 user_prompt 欄位
user_prompt = request.form.get("user_prompt")
# 向 LLM API發出 Request,得到回應 的result
# 將收到的 user_prompt 與 result傳給動態網頁 output.html
return render_template("output.html",
user_prompt=user_prompt)
```
 - ```(request.form).get("user_prompt")```
### Prompt
```xml
將<code>的代碼改寫成 Python的一段程式。
<code>
curl

"https://generativelanguage.googleapis.com/v1beta/models/gemini-
flash-latest:generateContent" \

-H 'Content-Type: application/json' \

-H 'X-goog-api-key: GOOGLE-API-KEY' \

-X POST \
-d '{
"contents": [
{
"parts": [
{
"text": "Explain how AI works in a few words"
}
]
}
]
}'
</code>
```

### 不要將API Key,帳號密碼寫死在Code內 (hard code),而是以組態方式設定或環境變數設定
 - ```API_KEY = os.getenv("GEMINI_API_KEY")``` -> 將 OS的環境變數 GEMINI_API_KEY 的值讀進 程式

### myapp.py 儲存在 ```C:\Users\weichih\standalone```
 - 開啟 ```Powshell``` 然後 ```cd``` 到 ```C:\Users\weichih\standalone```
 - ```python.exe myapp.py```
 - ```pip install requests```
 - ```$env:GEMINI_API_KEY="你的_API_KEY"```
 - ```export GEMINI_API_KEY="你的_API_KEY"```