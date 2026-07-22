import sys
from rag_service import KnowledgeBase, RAGService


def main():
    print("=" * 50)
    print("  技術知識庫 RAG 檢索系統 (CLI 測試介面)")
    print("  輸入 'exit' 或 'q' 即可離開程式")
    print("=" * 50)

    # 1. 初始化物件
    try:
        kb = KnowledgeBase("knowledge.txt")
        rag = RAGService(kb)
    except Exception as e:
        print(f"❌ 服務初始化失敗: {e}")
        sys.exit(1)

    # 2. 互動式搜尋 Loop
    while True:
        try:
            user_input = input("\n請輸入你的問題：").strip()

            if not user_input:
                continue

            if user_input.lower() in ["exit", "q", "quit"]:
                print("謝謝使用，再見！")
                break

            print("\n[系統] 檢索與生成中，請稍候...")
            result_html = rag.process_query(user_input)

            print("\n" + "-" * 20 + " 回應結果 (HTML) " + "-" * 20)
            print(result_html)
            print("-" * 57)

        except KeyboardInterrupt:
            print("\n程式已中斷。")
            break
        except Exception as e:
            print(f"❌ 發生錯誤: {e}")


if __name__ == "__main__":
    main()