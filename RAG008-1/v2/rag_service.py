import os
from pathlib import Path
import markdown
import requests
from dotenv import load_dotenv
from pinecone_store import PineconeVectorStore

# 載入環境變數
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


class RAGService:
    """
    RAG 檢索增強生成服務類別
    結合 PineconeVectorStore 搜尋相關背景上下文，並呼叫 Gemini LLM 生成答案。
    """

    def __init__(self, vector_store: PineconeVectorStore, console_flag: bool = True):
        """
        初始化 RAG 服務

        :param vector_store: PineconeVectorStore 的實例，提供語意搜尋功能
        :param console_flag: 控制是否在 Console 印出操作訊息 (預設 True 開啟)
        """
        self.vector_store = vector_store
        self.console_flag = console_flag
        self._log("=== [RAGService] 初始化開始 ===")

        # 讀取 Gemini API Key
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("找不到 GEMINI_API_KEY，請先在 .env 設定環境變數！")

        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"
        self._log("=== [RAGService] 初始化完成 ===\n")

    def _log(self, message: str):
        """[私有方法] 控制 Console 訊息列印的統一通道"""
        if self.console_flag:
            print(message)

    @staticmethod
    def markdown_to_html(md_text: str) -> str:
        """
        將 LLM 回傳的 Markdown 語法字串轉換成 HTML 格式

        :param md_text: Markdown 格式文字
        :return: HTML 格式字串
        """
        return markdown.markdown(
            md_text, extensions=["extra", "codehilite", "toc"]
        )

    def process_query(self, user_prompt: str) -> str:
        """
        處理使用者查詢的核心邏輯：
        1. 輸入檢驗
        2. 向 Vector DB 檢索知識庫 (Top K)
        3. 判斷是否有查到有效的 chunk_text：若無，直接回覆「無相關資料」不呼叫 LLM
        4. 若有相關資料，組裝包含 Context 的 System Prompt 呼叫 LLM 產生答案

        :param user_prompt: 使用者輸入的問題
        :return: HTML 渲染後的回覆字串
        """
        self._log("==========================================")
        self._log(f"[RAG 請求處理開始] 收到 Prompt: '{user_prompt}'")
        self._log("==========================================")

        # 防呆檢查：若輸入內容為空，提示輸入
        if not user_prompt or not user_prompt.strip():
            self._log("[警告] 輸入提問為空，中止流程。")
            return "<h1>請輸入有效的查詢問題。</h1><a href='/'>回提問頁</a>"

        # 步驟 1: 從 Pinecone Vector Database 搜尋 Top-3 相關文本
        search_results = self.vector_store.search_vector_database(
            user_prompt, top_k=3
        )

        # 提取有效（非 N/A）的 chunk_text
        chunk_texts = [
            # item["chunk_text"]
            ( "類別：" + item["category"] + "，內容：" + item["chunk_text"] + "，來源：" + item["source"])
            for item in search_results
            if item.get("chunk_text") and item.get("chunk_text") != "N/A"
        ]

        # 步驟 2: 當向量資料庫找不到相關 chunk_text 時，不與 LLM 提問，直接回覆「無相關資料」
        if not chunk_texts:
            self._log("[判斷結果] 未找到任何有效的 chunk_text。判定為「無相關資料」，跳過 LLM 提問步驟。")
            return "<h1>無相關資料</h1><p>知識庫中未找到與您提問相關的內容。</p><a href='/'>回提問頁</a>"

        # 步驟 3: 將取得的 chunk_text 組合成 context 字串
        self._log(f"[檢索成果] 找到 {len(chunk_texts)} 筆有效內容，進行 Context 組裝。")
        context_str = "。".join(chunk_texts)
        self._log(f"[Context 內容] {context_str}")

        # 步驟 4: 組裝送給 LLM 的 System Prompt
        system_prompt = (
            f"<user_prompt>{user_prompt}</user_prompt>"
            f"<context>{context_str}</context>"
            f"<specifier>從context找出user_prompt的答案，如果找不到就說不知道</specifier>"
        )

        # 步驟 5: 準備並呼叫 Gemini API
        self._log("正在發送 API 請求給 Gemini LLM...")
        headers = {
            "Content-Type": "application/json",
            "X-goog-api-key": self.api_key,
        }
        data = {"contents": [{"parts": [{"text": system_prompt}]}]}

        try:
            response = requests.post(
                self.api_url, headers=headers, json=data, timeout=15
            )
            response.raise_for_status()

            # 解析 API 回傳之 JSON 資料
            result = response.json()
            raw_text = result["candidates"][0]["content"]["parts"][0]["text"]
            self._log("[LLM 回應成功] 取得原始 Markdown 結果。")

            # 將 LLM 回傳的 Markdown 轉為 HTML 呈現
            html_output = self.markdown_to_html(raw_text)
            self._log("[RAG 請求處理成功結束]\n")
            return html_output

        except Exception as e:
            # 異常處理回覆
            self._log(f"[錯誤] 呼叫 Gemini API 發生例外異常: {e}")
            return f"<h1>系統呼叫發生錯誤：{str(e)}</h1><a href='/'>回提問頁</a>"