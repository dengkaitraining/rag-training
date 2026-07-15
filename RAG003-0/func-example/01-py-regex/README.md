### Prompt
```prompt
編寫一個Python 函式，給定 User_Prompt，函式會比對 User_Prompt是否有{AI, IoT, Blockchain}等關鍵字，如果有就return，若沒有比對到就return 空list。使用Python re Module，也就是 Regualr Expression Module。關鍵字如果是英文vocabulary的一部分視為未比對到，如果出現在非英文詞後就當做比對到。 
```
### Respose
這個需求非常務實！在處理中文和英文混雜（中英夾雜）的文本時，常會遇到一個痛點：

* 如果前面是**英文字母**（例如 `paint`），我們**不應該**算比對到 `AI`（因為它是英文單字的一部分）。
* 如果前面是**非英文字母**（例如中文字、標點符號、空格，像是 `這台IoT設備` 或是 `我對AI有興趣`），我們**應該**算比對到。

為了精準達到這個效果，我們不能只單純使用 `\b`（因為 `\b` 在中文字與英文字母之間不會判定為邊界）。

我們需要使用正規表示式的 **「零寬度斷言」（Lookbehind / Lookahead）**：

1. **左側限制（Lookbehind）**：關鍵字的左邊「不能是英文字母」 `(?<![a-zA-Z])`。
2. **右側限制（Lookahead）**：關鍵字的右邊「不能是英文字母」 `(?![a-zA-Z])`。

### 🐍 Python 實作程式碼

這裡為你設計好符合此規則的 Python 函式：

```python
import re

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

```

---

### 🧪 測試與驗證

我們準備了各種可能發生的邊界情況（Edge Cases）來測試這個函式：

```python
test_cases = [
    # 1. 出現於非英文詞（中文）後面 -> 應該比對到
    "這台IoT設備很棒", 
    "我對AI很有興趣",
    
    # 2. 出現於空格或標點符號後 -> 應該比對到
    "I like AI.",
    "Blockchain, IoT, and AI are trending.",
    
    # 3. 屬於英文單字的一部分 -> 應該忽略（未比對到）
    "Let's paint a picture.",        # paint 含有 ai -> 忽略
    "Biotech is expanding.",         # biotech 含有 iot -> 忽略
    "The blockchaining process...",  # blockchaining 含有 blockchain -> 忽略
    
    # 4. 混合極端情況
    "這是一個畫畫paint與AI的結合",    # 應只抓到 'AI'，忽略 'paint' 中的 ai
]

for text in test_cases:
    result = extract_tech_keywords(text)
    print(f"輸入: {text:<28} -> 偵測結果: {result}")

```

#### 輸出結果：

```text
輸入: 這台IoT設備很棒              -> 偵測結果: ['IoT']
輸入: 我對AI很有興趣              -> 偵測結果: ['AI']
輸入: I like AI.                 -> 偵測結果: ['AI']
輸入: Blockchain, IoT, and AI are trending. -> 偵測結果: ['Blockchain', 'IoT', 'AI']
輸入: Let's paint a picture.     -> 偵測結果: []
輸入: Biotech is expanding.      -> 偵測結果: []
輸入: The blockchaining process... -> 偵測結果: []
輸入: 這是一個畫畫paint與AI的結合    -> 偵測結果: ['AI']

```

### 💡 核心原理解析：

* `(?<![a-zA-Z])`：這是一個**否定後行斷言**（Negative Lookbehind）。它會檢查目前匹配位置的「左邊那一個字元」，只要左邊**不是**大寫 `A-Z` 或小寫 `a-z` 的英文字母，才允許匹配。這就完美解決了中文字（非英文詞）接英文關鍵字的問題。
* `(?![a-zA-Z])`：這是一個**否定先行斷言**（Negative Lookahead）。同樣道理，它檢查「右邊那一個字元」不能是英文字母，避免像 `blockchaining` 這樣往後延伸成其他英文字。