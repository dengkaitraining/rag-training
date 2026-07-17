### Prompt 1. 初次依據需求提出建立 docker compose 文件
```markdown
# 使用 docker compose 建立 Python Django Web base 資訊系統開發環境。
## 1. 應用套件與技術堆疊：
 - 網頁伺服器：apache httpd 伺服器。
 - 資料庫伺服器：MariaDB 伺服器。
 - 前端技術堆疊：TypeScript、Vue.js 框架、Tailwind CSS UI 套件。
 - 後端技術堆疊：Python Django 框架、Python Django Unfold 後台管理套件。
 - 資料庫連線技術：使用 Redis 技術以避免高併發的問題。
## 2. 技術堆疊容器化：
 - 將「1. 應用套件與技術堆疊」容器化，轉換為 docker compose 並建立下列文件資訊：
   - Dockerfile
   - docker-compose.yaml
   - .env
   ...
   等 docker compose 文件。
 - docker-compose.yaml 內 volumes 資料儲存目錄指向專案內實體路徑。
 - docker-compose.yaml 內加入 docker network bridge 網路連線。
 
## 3. 檢查 docker compose 文件
 - 檢查 docker compose 相關文件在 Linux , Windows 運行是否正確，並協助修補文件內容。
```
### Prompt 2. 更新所有套件與技術堆疊
```markdown
1. Vue 更新至 3.5。
2. Redis 更新至 8.8。
3. MariaDB 更新至 12.3。
4. Django 更新至 5.2。
5. Tailwind CSS UI 更新至 4.3。
```