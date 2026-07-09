<!--
![GitHub stars](https://img.shields.io/github/stars/dengkaitraining/rag-training?style=social)
![GitHub forks](https://img.shields.io/github/forks/dengkaitraining/rag-training?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/dengkaitraining/rag-training?style=social)
-->

![GitHub repo size](https://img.shields.io/github/repo-size/dengkaitraining/rag-training)
![GitHub language count](https://img.shields.io/github/languages/count/dengkaitraining/rag-training)
![GitHub top language](https://img.shields.io/github/languages/top/dengkaitraining/rag-training)
![GitHub last commit](https://img.shields.io/github/last-commit/dengkaitraining/rag-training?color=red)

## 「Python Flask 框架」與「檢索增強生成應用系統開發」課程範例
### 1. 建立 ```venv``` 開發與測試環境
| python 模組 | 說明 |
| :---| :--- |
| ```NumPy``` | ```NumPy (Numerical Python)```是 ```Python``` 語言中最核心的科學計算與資料處理第三方函式庫。它提供了強大的多維陣列```(ndarray)```物件與豐富的數學函式庫，是 ```Pandas```、```SciPy```、```Scikit-learn``` 及 ```TensorFlow``` 等巨量資料與人工智慧套件的重要基石。 |
| ```Flask``` | ```Flask``` 是使用 ```Python``` 撰寫的輕量級 ```Web``` 應用框架。因其精簡的核心被稱為「微框架」，具備高度彈性，開發者可自由組合資料庫或樣板引擎，只需簡單幾行程式碼即可架設網站或開發 ```API``` 服務。 |
| ```requests``` | ```requests``` 是 ```Python``` 中最受歡迎的 ```HTTP``` 請求套件之一。它的設計理念是「讓 ```HTTP``` 請求更簡單、更人性化」。開發者能輕鬆透過它發送 ```GET```、```POST``` 等請求來抓取網頁資料或與 ```API``` 互動，無需處理複雜的底層網路細節。 |
| ```Markdown``` | ```Python``` 與 ```Markdown``` 的結合主要可分為「使用 ```Python``` 解析 ```Markdown``` 語法」與「在 ```Python``` 生態系中撰寫 ```Markdown``` 文件」。 |
| ```python-dotenv``` | ```python-dotenv``` 是一個熱門的 ```Python``` 套件，主要用於讀取 ```.env``` 檔案中的設定，並將其自動載入為系統的環境變數。這能讓開發者將敏感資訊（如 ```API 金鑰```、```密碼```）與程式碼分離，避免敏感資料不慎外洩。 |
#### (1) Linux 開發測試環境
 - 1. 建立 python 虛擬環境。
```sh
# 不要使用 sudo 管理者權限安裝
# 建立 python 虛擬環境 venv
python -m venv venv
```
 - 2. 進入 / 離開 venv 虛擬環境
```sh
# 不要使用 sudo

# 1. 進入 venv 虛擬環境
source venv/bin/activate

# 2 離開 venv 虛擬環境
deactivate
```
 - 3. 安裝必要套件
```sh
# 不要使用 sudo 管理者權限安裝
python -m pip install numpy
python -m pip install flask
python -m pip install requests
python -m pip install markdown
python -m pip install dotenv
```
#### (2) Windows 開發測試環境
 - 1. 建立 python 虛擬環境。
```powershell
# 建立 python 虛擬環境 venv
python -m venv venv
```
 - 2. 進入 / 離開 venv 虛擬環境
```powershell
# 1. 進入 venv 虛擬環境
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1

# 2 離開 venv 虛擬環境
deactivate
```
 - 3. 安裝必要套件
```sh
python -m pip install numpy
python -m pip install flask
python -m pip install requests
python -m pip install markdown
python -m pip install dotenv
```