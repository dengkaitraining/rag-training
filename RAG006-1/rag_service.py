import os
import re
from pathlib import Path
import markdown
import requests
from dotenv import load_dotenv

# 讀取當前檔案所在目錄的 .env 檔案
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


class KnowledgeBase:
    """處理知識庫檔案讀取與檢索的類別"""

    def __init__(self, file_path: str = "knowledge.txt"):
        # 使用 pathlib.Path 確保檔案使用絕對路徑
        self.file_path = (BASE_DIR / file_path).resolve()
        self.line_pattern = re.compile(r'^\s*([^,]+?)\s*,\s*"(.*?)"\s*$')

    def find_by_keyword(self, keyword: str) -> list[str]:
        """從知識庫檔案中檢索關鍵字描述"""
        results = []

        if not self.file_path.exists():
            print(f"提示：找不到檔案 {self.file_path}")
            return results

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, 1):
                    line = line.strip()
                    if not line:
                        continue

                    match = self.line_pattern.match(line)
                    if match:
                        parsed_keyword = match.group(1)
                        description = match.group(2)

                        if parsed_keyword.lower() == keyword.lower():
                            results.append(description)
                    else:
                        print(f"警告：第 {line_number} 行格式不符，已跳過：{line}")

        except IOError as e:
            print(f"讀取檔案時發生錯誤: {e}")

        return results


class RAGService:
    """整合 RAG 流程與 API 呼叫的服務類別"""

    def __init__(self, knowledge_base: KnowledgeBase):
        self.kb = knowledge_base
        # 1. 讀取 .env 中的 API_KEY
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("找不到 GEMINI_API_KEY，請先在 .env 設定環境變數！")

        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"
        self.keyword_pattern = re.compile(
            r"(?<![a-zA-Z])(AI|IoT|Blockchain|AR|VR)(?![a-zA-Z])",
            flags=re.IGNORECASE,
        )

    def extract_keywords(self, user_prompt: str) -> list[str]:
        """萃取用戶提問中的技術關鍵字"""
        return self.keyword_pattern.findall(user_prompt)

    @staticmethod
    def markdown_to_html(md_text: str) -> str:
        """Markdown 轉 HTML"""
        return markdown.markdown(
            md_text, extensions=["extra", "codehilite", "toc"]
        )

    def process_query(self, user_prompt: str) -> str:
        """處理查詢的核心主邏輯"""
        matches = self.extract_keywords(user_prompt)
        if not matches:
            return "<H1>你的問題太高深了，本仙人功力不足以回答。</H1><a href='/'>回提問頁</a>"

        search_str = matches[0]

        # 檢索知識庫
        ai_results = self.kb.find_by_keyword(search_str)
        context_str = "。".join(ai_results)

        # 組裝 Prompt
        system_prompt = (
            f"<user_prompt>{user_prompt}</user_prompt>"
            f"<context>{context_str}</context>"
            f"<specifier>從context找出user_prompt的答案，如果找不到就說不知道</specifier>"
        )

        # 呼叫 Gemini API
        headers = {
            "Content-Type": "application/json",
            "X-goog-api-key": self.api_key,
        }
        data = {"contents": [{"parts": [{"text": system_prompt}]}]}

        response = requests.post(
            self.api_url, headers=headers, json=data, timeout=15
        )
        response.raise_for_status()

        result = response.json()
        raw_text = result["candidates"][0]["content"]["parts"][0]["text"]

        return self.markdown_to_html(raw_text)


# Flask App 整合範例 (可視情況取消註解或獨立放於 app.py)
"""
from flask import Flask, render_template, request

app = Flask(__name__)
rag_service = RAGService(KnowledgeBase("knowledge.txt"))

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/process", methods=["POST"])
def process():
    user_prompt = request.form.get("user_prompt", "")
    outstr = rag_service.process_query(user_prompt)
    return render_template("output.html", user_prompt=user_prompt, result=outstr)
"""