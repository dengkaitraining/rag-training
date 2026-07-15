### Prompt
```prompt
編寫一個Python 函式，給定關鍵字可以到純文字檔 knowledge.txt找出對應的內容。
純文字檔 knowledge.txt 是 {關鍵字, 描述}的結構，每一行儲存一筆關鍵字資訊，每一個關鍵字包含多個描述內容。描述是以"與"包含起來，儲存內容舉例如下：
AI, "Artificial Intelligent, 主要分鑑別式AI與生成式AI"
IoT,"Internet of Things, 全面感知、數據處理、決策控制"
AI, "資料探勘有時也被稱為AI"
IoT,"各類感測器是蒐集數據的IoT終端裝置"
AI, "基因演算法這一類的最佳解搜尋也被稱為AI"
```
### Response
```python
# Let's test the parser logic
import re

# Sample data representation
sample_data = """AI, "Artificial Intelligent, 主要分鑑別式AI與生成式AI"
IoT,"Internet of Things, 全面感知、數據處理、決策控制"
AI, "資料探勘有時也被稱為AI"
IoT,"各類感測器是蒐集數據的IoT終端裝置"
AI, "基因演算法這一類的最佳解搜尋也被稱為AI"
"""

def search_knowledge(keyword, file_content):
    results = []
    # Regular expression to match: Keyword, "Description"
    # We want to handle optional spaces around comma and quotes.
    pattern = re.compile(r'^\s*([^,\s]+)\s*,\s*"(.*)"\s*$', re.MULTILINE)
    for match in pattern.finditer(file_content):
        kw, desc = match.groups()
        if kw.strip().lower() == keyword.strip().lower():
            results.append(desc)
    return results

print(search_knowledge("AI", sample_data))
print(search_knowledge("IoT", sample_data))


```

```text
['Artificial Intelligent, 主要分鑑別式AI與生成式AI', '資料探勘有時也被稱為AI', '基因演算法這一類的最佳解搜尋也被稱為AI']
['Internet of Things, 全面感知、數據處理、決策控制', '各類感測器是蒐集數據的IoT終端裝置']


```

這個需求非常適合使用 Python 的 `re`（正規表示式）模組來解析。

由於 `knowledge.txt` 的結構類似 CSV，但描述內容中可能包含逗號，且描述是以雙引號 `"` 包裹起來的。我們可以使用正規表示式精準抽離出每一行的**關鍵字**與**雙引號內的描述**，並將結果收集起來。

### 🐍 Python 實作程式碼

以下為你編寫的 Python 函式 `search_knowledge_by_keyword`：

```python
import re
import os

def search_knowledge_by_keyword(keyword: str, file_path: str = "knowledge.txt") -> list:
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

```

---

### 🧪 測試說明

假設你的目錄下已有一個 `knowledge.txt`，內容如下：

```text
AI, "Artificial Intelligent, 主要分鑑別式AI與生成式AI"
IoT,"Internet of Things, 全面感知、數據處理、決策控制"
AI, "資料探勘有時也被稱為AI"
IoT,"各類感測器是蒐集數據的IoT終端裝置"
AI, "基因演算法這一類的最佳解搜尋也被稱為AI"

```

你可以使用以下程式碼來進行測試：

```python
# 1. 搜尋關鍵字 "AI"
ai_results = search_knowledge_by_keyword("AI")
print("【AI 的搜尋結果】:")
for idx, desc in enumerate(ai_results, 1):
    print(f"{idx}. {desc}")

print("-" * 50)

# 2. 搜尋關鍵字 "IoT" (測試小寫輸入是否能對應)
iot_results = search_knowledge_by_keyword("iot")
print("【IoT 的搜尋結果】:")
for idx, desc in enumerate(iot_results, 1):
    print(f"{idx}. {desc}")

print("-" * 50)

# 3. 搜尋不存在的關鍵字 "Blockchain"
blockchain_results = search_knowledge_by_keyword("Blockchain")
print(f"【Blockchain 的搜尋結果】: {blockchain_results}")

```

#### 輸出結果：

```text
【AI 的搜尋結果】:
1. Artificial Intelligent, 主要分鑑別式AI與生成式AI
2. 資料探勘有時也被稱為AI
3. 基因演算法這一類的最佳解搜尋也被稱為AI
--------------------------------------------------
【IoT 的搜尋結果】:
1. Internet of Things, 全面感知、數據處理、決策控制
2. 各類感測器是蒐集數據的IoT終端裝置
--------------------------------------------------
【Blockchain 的搜尋結果】: []

```

### 💡 核心設計解析

1. **防呆與空白容錯**：`\s*` 可以容許檔案中逗號前後有不小心的空格（例如：`AI , "..."` 或 `AI,   "..."`），確保解析時不會因為排版而失敗。
2. **非貪婪與精準對應**：使用 `"(.*)"` 確保完美抓取雙引號內的所有文字（即便描述裡包含中英夾雜或逗號），不影響關鍵字本身的判讀。
3. **大小寫友善比對**：函式預設採用 `.lower()` 來比對，因此就算使用者輸入小寫的 `iot` 或 `ai`，也能正確找到大寫開頭的資料。


### Prompt
```prompt
編寫一個Python 函式，給定關鍵字可以到純文字檔 knowledge.txt找出對應的內容。
1. 加入 from pathlib import Path 模組，knowledge.txt 與煮成是在同一資料夾內，使用絕對路徑存取檔案。
2. 純文字檔 knowledge.txt 是 {關鍵字, 描述}的結構，每一行儲存一筆關鍵字資訊，每一個關鍵字包含多個描述內容。描述是以"與"包含起來，儲存內容舉例如下：
AI, "Artificial Intelligent, 主要分鑑別式AI與生成式AI"
IoT,"Internet of Things, 全面感知、數據處理、決策控制"
AI, "資料探勘有時也被稱為AI"
IoT,"各類感測器是蒐集數據的IoT終端裝置"
AI, "基因演算法這一類的最佳解搜尋也被稱為AI"
```
### Response
這個版本為你加入了 Python 的 `pathlib.Path` 模組，並利用它來定位「主程式所在的資料夾」，進而取得 `knowledge.txt` 的**絕對路徑**。

這樣做的好處是：不論你是在哪一個工作目錄下執行這個 Python 檔，它都能精確找到與主程式放在同一個資料夾底下的 `knowledge.txt`，徹底避免「找不到檔案（FileNotFoundError）」的問題！

### 🐍 Python 實作程式碼

```python
import re
from pathlib import Path

def search_knowledge_by_keyword(keyword: str) -> list:
    """
    使用絕對路徑讀取與主程式同目錄下的 knowledge.txt，
    並從中搜尋與給定關鍵字相符的所有描述。
    
    :param keyword: 欲搜尋的關鍵字（例如 'AI' 或 'IoT'）
    :return: 包含所有對應描述內容的 list。若無比對到或檔案不存在，則回傳空 list []。
    """
    # 1. 取得主程式（目前檔案）所在的資料夾絕對路徑
    current_dir = Path(__file__).resolve().parent
    
    # 2. 組合出 knowledge.txt 的絕對路徑
    file_path = current_dir / "knowledge.txt"
    
    # 檢查檔案是否真的存在
    if not file_path.exists():
        print(f"錯誤：在絕對路徑找不到檔案：{file_path}")
        return []
        
    results = []
    
    # 正規表示式解析規則：
    # ^\s*([^,\s]+)  : 匹配關鍵字（不包含逗號與空白）
    # \s*,\s*        : 匹配關鍵字與雙引號之間的逗號（容許前後有空白）
    # "(.*)"\s*$     : 精準抓取被雙引號 " " 包裹起來的「描述內容」
    pattern = re.compile(r'^\s*([^,\s]+)\s*,\s*"(.*)"\s*$')
    
    # 使用絕對路徑開啟檔案
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
                
            # 使用 re 比對
            match = pattern.match(line)
            if match:
                file_keyword, description = match.groups()
                
                # 進行不區分大小寫的比對
                if file_keyword.strip().lower() == keyword.strip().lower():
                    results.append(description)
                    
    return results

```

---

### 💡 核心技術說明：

1. **`Path(__file__)`**：代表「目前這個 Python 檔案」的路徑。
2. **`.resolve()`**：將路徑轉換成「絕對路徑」，排除掉所有的相對路徑符號（如 `.` 或 `..`）。
3. **`.parent`**：取得該檔案所在的「上層資料夾路徑」。
4. **`current_dir / "knowledge.txt"`**：`pathlib` 提供非常直覺的 `/` 運算子，能自動幫我們根據作業系統（Windows 用 `\`，Mac/Linux 用 `/`）組合成正確的檔案絕對路徑。