Agent Skills 是一種模組化的 AI 工作說明書，用來規範 AI 在特定任務中的判斷流程、工具使用與輸出格式。 [1, 2, 3] 
這套結構最初由 [Anthropic](https://claude-world.com/zh-tw/articles/anthropic-official-skills-complete-guide/) 與 Google (ADK) 等科技巨頭推動，其核心目的在於讓 AI Agent 能具備可攜式、可重複利用且漸進式載入的領域專業知識。 [3, 4] 

------------------------------
## 📂 Agent Skills 的標準目錄結構
一個完整的 Agent Skill 基本上是一個獨立的資料夾，內部主要包含以下內容：

* SKILL.md：核心指令檔案。
* scripts/：選用的自動化腳本。
* examples/：可供 AI 參考的範例。

------------------------------
## 📝 SKILL.md 核心範本
以下是撰寫 SKILL.md 的標準 Markdown 範本，它包含了確保 AI 準確觸發與執行的 5 大關鍵要素：

```markdown
# [技能名稱：例如 YouTube 趨勢分析專家]
## Description<!-- 關鍵！描述此技能「何時」該被觸發。AI 會依據這段文字決定是否載入本技能 -->
當使用者需要分析 YouTube 影片趨勢、整理市場熱門話題、或是需要將特定主題的觀看數據產出為結構化摘要時，觸發此技能。
## Instructions<!-- 核心 SOP：規範 AI 的思考與執行步驟 -->1. 思考與規劃：在執行前，先列出需要分析的目標領域與關鍵字。
2. 收集資料：使用 [網頁搜尋/指定工具] 撈取近 30 天內觀看量前 10 名的相關影片。3. 數據歸納：分析這些熱門影片的標題痛點、縮圖風格與內容架構。4. 排除雜訊：自動過濾廣告、業配文或與主題無關的點閱干擾。
## Input Format<!-- 規範使用者或系統傳入的資料格式 -->
使用者必須提供：- 關鍵字或目標領域（例如：AI 自動化）- 期望分析的時間區間（預設為 30 天）
## Output Format<!-- 嚴格規範輸出格式，確保自動化管線不會出錯 -->
請務必依據以下 Markdown 格式輸出，嚴禁提供額外的問候語：### 1. 熱門主題趨勢- **主題名稱**：[簡短描述]
- **熱門原因**：[分析消費者痛點]
### 2. 優化建議- [具體可執行的下一步行動]
## Constraints & Rules<!-- 設定 AI 絕對不能踩的紅線 -->- 嚴禁捏造數據，若查無資料必須主動說明。- 輸出的優化建議不得超過 3 項。- 專有名詞一律使用繁體中文（台灣）慣用語。
```
------------------------------
## 🔑 撰寫 Agent Skills 的 4 大重要內容
要寫出高效的 Agent Skill，必須掌握以下重點：

   1. 精準的 Description（觸發詞）
   * AI Agent 是透過 Description 來辨識何時要調用這個 Skill。
      * 文字必須具體，避免使用「我能幫你做很多事」等模糊字眼。 [5, 6] 
   2. 漸進式揭露（Progressive Disclosure）
   * 不要把所有規則塞在同一個 System Prompt 裡。
      * 透過 Skill 封裝，讓 AI「需要時再載入」對應的上下文即可。
   3. 嚴格的輸出格式約束（Output Format）
   * 若此技能要對接其他軟體（如自動產生簡報、寄出 Email），格式必須絕對固定。
      * 建議在 Output Format 中要求 AI 排除前後的社交客套話。 [3, 7, 8] 
   4. 提供 Few-shot 範例（Examples）
   * 在資料夾中附帶正確的輸入與輸出範例（例如 examples/good_output.md）。
      * 這比寫一堆規則更能有效引導 AI 產出高品質的成果。
   
------------------------------
如果想進一步實作，您可以告訴我：

* 您打算建立哪種場景的 AI 技能（例如：SEO 寫作、代碼審查、會議摘要等）？
* 您預計會整合哪些外部工具或 API？

我可以為您量身打造專屬的 SKILL.md 內容！

[1] [https://www.bnext.com.tw](https://www.bnext.com.tw/article/90058/agent-skills-free-course-deeplearning-ai-anthropic-latest-partnership)
[2] [https://yujing.io](https://yujing.io/articles/what-is-agent-skill/)
[3] [https://marketing.91app.com](https://marketing.91app.com/agent-ai-skill-marketing-guide/)
[4] [https://learn.microsoft.com](https://learn.microsoft.com/zh-tw/agent-framework/agents/skills)
[5] [https://medium.com](https://medium.com/@simon3458/agent-%E5%91%8A%E5%88%A5%E8%90%BD%E8%90%BD%E9%95%B7%E7%9A%84-prompt-google-adk-agent-skill-%E5%8A%9F%E8%83%BD%E5%AF%A6%E6%88%B0%E8%A7%A3%E6%9E%90-2eeecf69ed4f)
[6] [https://blog.wu-boy.com](https://blog.wu-boy.com/2026/03/what-is-agent-skill-and-impact-on-software-industry-zh-tw/)
[7] [https://www.bnext.com.tw](https://www.bnext.com.tw/article/90186/what-is-agent-skill)
[8] [https://www.threads.com](https://www.threads.com/@hei_ai.automation/post/DUC6P9LEzA8/%E5%BB%BA%E7%AB%8B-agent-skills-%E7%9A%84-5-%E5%80%8B%E6%A0%B8%E5%BF%83%E9%87%8D%E9%BB%9E-1-%E4%BA%86%E8%A7%A3%E6%B8%85%E6%A5%9A%E9%9C%80%E6%B1%822-%E4%B8%BB%E5%8B%95%E8%B7%9F-ai-%E8%92%90%E8%AD%893-%E4%B8%80%E9%82%8A%E5%81%9A%E4%B8%80%E9%82%8A%E6%94%B9%E4%B8%8D%E8%BF%BD%E6%B1%82%E5%AE%8C%E7%BE%8E4-%E5%96%84%E7%94%A8%E7%B6%B2%E8%B7%AF%E7%A0%94%E7%A9%B6%E8%B3%87%E6%BA%905-%E8%80%90%E5%BF%83%E8%A8%93%E7%B7%B4%E5%83%8F%E6%95%99%E6%96%B0%E5%93%A1%E5%B7%A5%E5%85%B6)
