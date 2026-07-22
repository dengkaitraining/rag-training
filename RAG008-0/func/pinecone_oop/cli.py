import sys
from pathlib import Path
from pinecone_store import PineconeVectorStore

# 取得根目錄與預設 JSON 路徑
BASE_DIR = Path(__file__).resolve().parent
DEFAULT_JSON_PATH = BASE_DIR / "data.json"


def print_menu():
    print("\n" + "=" * 30)
    print(" Pinecone Vector DB CLI 工具 ")
    print("=" * 30)
    print("1. 匯入/建立向量資料庫 (從 data.json)")
    print("2. 進行語意搜尋")
    print("0. 離開程式")
    print("=" * 30)


def main():
    try:
        store = PineconeVectorStore()
    except Exception as e:
        print(f"初始化錯誤：{e}")
        sys.exit(1)

    while True:
        print_menu()
        choice = input("請選擇操作 (0-2): ").strip()

        if choice == "1":
            file_input = input(f"請輸入 JSON 檔案路徑 (預設: {DEFAULT_JSON_PATH.name}): ").strip()
            target_path = Path(file_input).resolve() if file_input else DEFAULT_JSON_PATH

            try:
                store.build_vector_database(json_path=target_path)
            except Exception as e:
                print(f"\n[錯誤] 建立過程失敗：{e}")

        elif choice == "2":
            query = input("\n請輸入搜尋問題：").strip()
            if not query:
                print("問題不能為空！")
                continue
            
            top_k_input = input("請輸入 Top K 數量 (預設 3): ").strip()
            top_k = int(top_k_input) if top_k_input.isdigit() else 3

            try:
                store.search_vector_database(query=query, top_k=top_k)
            except Exception as e:
                print(f"\n[錯誤] 搜尋過程失敗：{e}")

        elif choice == "0":
            print("\n感謝使用，再見！")
            break
        else:
            print("無效選項，請重新選擇。")


if __name__ == "__main__":
    main()