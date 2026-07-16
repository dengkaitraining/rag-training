這是一個完整的 Agent Skill 資料夾範本。此架構遵循了 Anthropic 與 Google ADK 的模組化規範，完美融合了您提到的 Description、Instructions、scripts、reference、examples 這 5 大核心要素，讓 AI Agent 能夠精準辨識、載入並執行特定任務。

------------------------------
## 📂 1. 檔案目錄結構設計
在專案中，一個標準的 Agent Skill 檔案結構通常如下：
```bash
skills/
└── market-research-expert/          # 技能資料夾名稱
    ├── SKILL.md                     # 核心說明書 (包含 Description、Instructions)
    ├── scripts/
    │   └── fetch_competitor_data.py # 自動化執行或輔助 AI 的 Python 腳本
    ├── reference/
    │   └── report_template.json     # 格式定義或背景知識庫參考
    └── examples/
        ├── input_sample.txt         # 使用者輸入範例
        └── output_sample.md         # AI 理想輸出範例
```
------------------------------
## 📝 2. SKILL.md 核心說明書範本
```markdown
# 技能名稱：市場競品分析專家 (Market Research Expert)

## Description<!-- 關鍵：定義此技能的觸發情境，AI 透過此段文字決定是否載入本技能 -->
當使用者提供特定產品、產業關鍵字或品牌名稱，並要求進行「競品調查」、「市場趨勢分析」、「優劣勢評估 (SWOT)」或「產品定位研究」時，觸發此技能。

## Instructions<!-- 核心 SOP：規範 AI 的思考邏輯、步驟與工具調用順序 -->
1. **解析目標**：提取使用者輸入的品牌或產品名稱，識別其核心產業類別。
2. **調用腳本**：自動執行 `scripts/fetch_competitor_data.py` 獲取該產業前 3 大競品數據，或使用 [網頁搜尋工具] 撈取最新資料。
3. **框架分析**：依據 `reference/report_template.json` 規定的結構進行多維度對比。
4. **排除干擾**：過濾掉重複的業配新聞、非正式論壇閒聊，僅保留具參考價值的財報、官方產品規格或權威評測。
5. **生成報告**：依據 `examples/output_sample.md` 的風格，產出結構化的中文分析。

## Input Format使用者必須提供：
 - `target_product`: 欲分析的產品或品牌名稱（必填）
 - `market_region`: 目標市場區域，如：台灣、北美（選填，預設為台灣）
## Output Format請嚴格依據 `examples/output_sample.md` 的 Markdown 格式輸出，嚴禁包含任何「好的，我幫你分析」等客套廢話。

## Constraints & Rules- 嚴禁憑空捏造市場數據，查無資料時必須明確回報。
 - 競品對比數量上限為 3 家。
 - 所有專有名詞需使用繁體中文（台灣）慣用語。
```
------------------------------
## 💻 3. scripts/ 範例：自動化腳本
此腳本由 AI 在執行 Instruction 步驟 2 時自動調用（通常由 Agent 框架執行），用來擴展 AI 的能力上限。
檔案位置：scripts/fetch_competitor_data.py
```python
import sysimport json
def fetch_data(target):
    # 模擬調用外部 API 或搜尋引擎獲取數據
    mock_database = {
        "智慧手錶": ["Apple Watch", "Garmin Venu", "Samsung Galaxy Watch"],
        "電動車": ["Tesla Model 3", "BYD Seal", "Hyundai IONIQ 5"]
    }
    return mock_database.get(target, ["競品 A", "競品 B", "競品 C"])
if __name__ == "__main__":
    # 接收 AI 傳入的參數
    input_target = sys.argv[1] if len(sys.argv) > 1 else "智慧手錶"
    results = fetch_data(input_target)
    # 將結構化結果返回給 AI
    print(json.dumps({"competitors": results}))
```
------------------------------
## 📑 4. reference/ 範例：靜態參考資料
用來約束 AI 輸出的資料結構，或是提供不可更動的商務背景知識。
檔案位置：reference/report_template.json
```json
{
  "required_sections": [
    "競品基本資料",
    "核心優勢分析",
    "潛在威脅與痛點"
  ],
  "allowed_metrics": ["價格區間", "主打功能", "使用者評價"]
}
```
------------------------------
## 🎯 5. examples/ 範例：Few-shot 少樣本學習
提供標準答案，這是讓 AI 輸出「不跑偏」最強大的關鍵要素。
檔案位置：examples/output_sample.md
```markdown
### 📊 [產品名稱] 競品分析報告

#### 1. 核心競品清單
 - **競品 A**：[名稱]（市場份額估計：XX%）
 - **競品 B**：[名稱]（市場份額估計：XX%）

#### 2. 多維度對比
| 評估維度 | 本品特色 | 競品 A | 競品 B |
| :--- | :--- | :--- | :--- |
| **價格** | 中價位 | 高價位 | 低價位 |
| **優勢** | 續航力長 | 品牌生態圈 | 性價比高 |

#### 3. 行動建議- [具體可執行的一句話建議]
```
------------------------------
## 💡 如何發揮這個範本的最大威力？

   1. Description 寫法是靈魂：AI Agent 在運行時，會用 Embedding 去比對使用者的問題與這裡的 Description。如果寫得太模糊（例如：「我能幫你分析各種東西」），AI 就容易「抓錯技能」或「漏載技能」。
   2. 維持 scripts 的高單一性：一個 Skill 的腳本通常只解決一件事（如：撈資料、算數據），複雜的邏輯交給 AI 配合 Instruction 來判斷。
   3. Reference 不要塞大檔案：參考資料最好是乾淨的 JSON、CSV 或小型的 Markdown 規則。

您可以告訴我您目前正在開發的 AI Agent 具體應用場景（例如：客服自動化、自動代碼審查、社群文案生成），我可以直接為您生成該場景的完整套裝檔案內容！

