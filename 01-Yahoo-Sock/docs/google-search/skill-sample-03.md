Agent Skill（代理技能）是一個包含指令、腳本與資源的資料夾結構，其標準的檔案管理架構包含主說明檔（通常為 SKILL.md）、執行腳本、參考資料及範例。當 AI Agent 偵測到使用者任務符合該技能的 Description 時，便會動態載入此技能包來精準執行任務。
以下為您提供一個完整的 Agent Skill 專案目錄結構與 SKILL.md 的標準範本。

------------------------------
## 📂 Agent Skill 目錄結構範例
一個標準的 Agent Skill 資料夾（例如一個名為 data-exporter 的技能）會長這樣：
```bash
data-exporter/
├── SKILL.md             # 核心定義檔（包含 Description 與 Instructions）
├── scripts/             # 放 AI 可以執行或呼叫的自動化腳本
│   └── export_csv.py    # 範例：將資料轉為 CSV 的 Python 腳本
├── reference/           # 供 AI 查閱的領域知識、API 文件或商業規則
│   └── schema_rules.json# 範例：資料欄位格式限制規範
└── examples/            # 實例示範（Few-Shot 範例），讓 AI 依循格式
    ├── input.json       # 範例輸入
    └── output.csv       # 範例輸出
```
------------------------------
## 📄 SKILL.md 核心範本
這是放在技能根目錄下的核心描述檔，通常採用 Front Matter 格式定義元數據（Metadata）：
```markdown
---
name: data-exporterdescription: 用於處理原始 JSON 資料，並根據內部欄位規範將其轉換、清理、匯出為標準 CSV 檔案。當使用者要求「匯出報告」、「轉換資料格式」或「清理欄位」時，應觸發此技能。
---

# Instructions（操作指令）
 你是一個專業的資料處理代理。當此技能被觸發時，請嚴格按照以下步驟執行任務：
 1. **驗證輸入**：檢查使用者提供的原始資料是否為有效的 JSON 格式。若格式錯誤，請立即中止並回報原因。
 2. **查閱規範**：讀取 `reference/schema_rules.json` 中的欄位規則，確認哪些欄位需要保留、去識別化或進行型態轉換。
 3. **執行轉換腳本**：調用 `scripts/export_csv.py` 腳本，將驗證過的 JSON 資料傳入。4. **錯誤處理**：如果腳本執行期間拋出錯誤，請根據錯誤訊息修正資料，最多嘗試重試 2 次。
 5. **輸出確認**：確保輸出的 CSV 檔案結構與 `examples/output.csv` 一致，並將下載連結或檔案內容呈現給使用者。
## 輸出格式規範- 所有的日期格式必須統一為 `YYYY-MM-DD`。
 - 金額欄位若為空值，一律填入 `0`。
---
# Scripts / 腳本說明的上下文AI 可視需求調用 `scripts/` 資料夾下的工具。本技能提供：
 - `scripts/export_csv.py`: 接受一個 JSON 字串，並自動輸出一個清理後的 CSV 流。
---

# Reference / 參考資料本技能內建以下規則庫，執行時請優先遵循：
 - 請參閱 `reference/schema_rules.json` 以獲取最新的客戶隱私去識別化（Data Masking）標準（例如：手機號碼需遮蔽中 4 碼）。
---

# Examples / 實例示範

### 範例 1：標準轉換**User Input (Data):**
```json
[
  {"user_id": 101, "name": "Alex", "join_date": "2026/07/16", "phone": "0912345678"}
]
```
**Agent Output / Action:**
1. 讀取 `reference/schema_rules.json` 發現 `phone` 需要遮蔽，`join_date` 格式需修正。
2. 執行 `scripts/export_csv.py`。3. 產生最終符合規範的 CSV 內容：
```csv
user_id,name,join_date,phone
101,Alex,2026-07-16,0912****78
```
```
------------------------------
## 🛠 附錄：其他輔助檔案內容範例
為了讓整個技能夾能真正跑起來，您的 scripts/ 和 reference/ 可以這樣寫：
## 1. scripts/export_csv.py (Python 腳本範例)
```python
import sysimport jsonimport pandas as pd
def main():
    # 接收 AI 傳進來的 JSON 字串
    input_data = sys.argv[1]
    data = json.loads(input_data)
    
    # 轉換成 DataFrame 並匯出
    df = pd.DataFrame(data)
    df.to_csv('output.csv', index=False)
    print("CSV generated successfully.")
if __name__ == "__main__":
    main()
```
## 2. reference/schema_rules.json (商務規則範例)
```json
{
  "required_fields": ["user_id", "name"],
  "date_format": "%Y-%m-%d",
  "masking_rules": {
    "phone": "mask_middle_4_digits"
  }
}
```
------------------------------
如果您想針對特定平台（例如 Anthropic, Microsoft Agent Framework, Salesforce）撰寫特定格式，可以告訴我您目前正在使用哪一套 AI Agent 框架，以便為您精準調整語法！ [1] 

[1] [https://learn.microsoft.com](https://learn.microsoft.com/zh-tw/agent-framework/agents/skills)
