### MySQL 是 DB Server，管理Databases。Database 可以包含多個Tables。
 - 每個Table由欄位構成，將各欄位填入值，就叫一筆資料紀錄(record)。
 - Tables 之間以Primary Key (主鍵)與 Foreign Key(外來鍵，其他Table的主鍵)關聯在一起，因此叫做關聯式資料庫。

### MySQL 可以單獨安裝，也可以跟其他工具一起安裝，例如 Apperv Web Server。它們都是Open Source。
### Apperv Web Server 的安裝
1. search "Apperv download"
2. 執行安裝檔，一步一步，其中有一步要設定MySQL 的管理密碼，也就是 root 的密碼，務必記下來。
3. http://127.0.0.1/ 確認是否安裝成功
4. Appserv 的程式語言是php。
5. Appserv 工具包有一個php網站，叫 phpMyAdmin ，專門用來管理MySQL DB的GUI，
    http://127.0.0.1/phpMyAdmin/ 就可以連到。 
	
### php Web Application
 - web site 在 C:\AppServ\www  C:\AppServ 可以換，但 www 是內建的
 - AppServ 是 Windows OS下的服務
 -  http://127.0.0.1/  是   http://127.0.0.1:80/index.php 的省略，index.php就是Homepage。
 -  在Browser輸入  http://127.0.0.1:80/index.php 就是  invoke index.php 在Web Server端的執行，執行後，
    有一個 echo 或 print 命令，會將HTML字串(就是HTML dicument包含HTML、CSS、Javascript)response到Browser，Browser
	呈現頁面結果。
 -  http://127.0.0.1/phpMyAdmin/ 是 http://127.0.0.1:80/phpMyAdmin/index.php
 - php 指令(statement)要包含在 ```<?php``` 與 ```?>``` 之間
 
 ### 資料庫與資料表及資料紀錄建好了，有3種管理資料的方式
 - A. GUI (Graphic User Interface)，可以是  Web Application 或 Win Form(視窗) - http://127.0.0.1/phpMyAdmin/ 是 MySQL 的 GUI
 - B. CLI (Comman Line Interface)，在cmd 或  PowerShell 執行 CLI client ，例如 mysql.exe 
```bash
C:\Users\user>mysql.exe -u root -p
Enter password: #########*
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 208
Server version: 8.0.17 MySQL Community Server - GPL

Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use chunk
Database changed
mysql> select * from imychunk;
+ - - --+ - - - --+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+
| ID    | keyword | content                                                                                  |
+ - - --+ - - - --+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+
| C1000 | AI      | 人工智慧，分Discrimiratic AI 與 Generative AI                                            |
| C2000 | AI      | Artificial Intelligence ， Rule Based 是很早以前的技術，現在是生成式AI s                 |
+ - - --+ - - - --+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+
2 rows in set (0.00 sec)

 - SQL 指令的最後都要以 ; 結束。如果沒有; mysql.exe 視為命令未結束，...

mysql> select * from imychunk;
從資料表 imychunk 查詢所有資料紀錄(無查詢條件)，每一個欄位都要。

mysql> select keyword, content from imychunk;
從資料表 imychunk 查詢所有資料紀錄，只要keyword, content欄位。
```
** 條件查詢  使用 where 條件
```bash
select * from imychunk where ID="C1000";
```
 - 查詢出 ID等於C1000的資料紀錄，所有欄位都要。
```bash
select content from imychunk where keyword="AI";
mysql> select content from imychunk where keyword="AI";
+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+
| content                                                                                  |
+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+
| 人工智慧，分Discrimiratic AI 與 Generative AI                                            |
| Artificial Intelligence ， Rule Based 是很早以前的技術，現在是生成式AI s                 |
+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+
2 rows in set (0.00 sec)
```
** 管理資料庫的過程
1. 連到 ```Mysql Server```，```mysql.exe -u root -p``` - 帳號與密碼
2. 決定要管理那一個資料庫, ```mysql> use chunk```
3. ```select``` 查詢語法 ```select content from imychunk where keyword="AI";```

### schema (綱要)
```Table name: imychunk```
欄位有3個： ```ID```、```keyword```、```content```，資料型態分別是 ```CHAR(6)```、```CHAR(20)```、```text```

C. 程式內嵌SQL指令
### Prompt 1
```
有一個資料庫 chucnk，綱要如<schema>所述。資料庫管理系統為 MySQL，管理帳號為 root 與  A123456789。
MySQL Server安裝在local。編寫一個Python Flask Web Application，具有<spec>的功能。
<spec>
 1. 有一個表單，可以選擇欄位之後，對後端發出資料庫查詢動作。
 2. 欄位可以多選。
 3. 表單為單獨的靜態網頁。
 4. 查詢結果網頁使用動態網頁。
 5. 不使用CSS與Javascript語法。
</spec>
<schema>
 Table name: imychunk
 欄位有3個： ID、keyword、content，資料型態分別是 CHAR(6)、CHAR(20)、text
</schema>
```

### Vibe Coding
 - 要能 Debug
 - 要能修改
 - 要能擴充

### Prompt 2
```
有一個資料庫 chunk，綱要如<schema>所述。資料庫管理系統為 MySQL，管理帳號為 root 與  A123456789。
MySQL Server安裝在local。編寫一個Python Flask Web Application，具有<spec>的功能。
<spec>
 1. 有一個表單，選擇欄位之後，可填入欄位值，對後端發出資料庫查詢動作。
 2. 若所輸入的欄位值，查詢不到資料，顯示 "查無資料"。
 2. 欄位可以多選。
 3. 表單為單獨的靜態網頁。
 4. 查詢結果網頁使用動態網頁。
 5. 不使用CSS與Javascript語法。
</spec>
<schema>
 Table name: imychunk
 欄位有3個： ID、keyword、content，資料型態分別是 CHAR(6)、CHAR(20)、text
</schema>
```
### 以關鍵字對資料表某欄位的內容進行全文檢索 
```sql
SELECT * FROM Customers
WHERE CustomerName LIKE 'An%';
```
 -> 將資料表 Customers的資料紀錄中的CustomerName欄位，有以"An"開頭的資料紀錄都查詢出來 

### 指令縮寫
1.
```php
sql += "where"
``` 
就是
```php
sql = sql + "where"
```
2. ```a+=2``` 就是  ```a=a+2```

3. ```a++``` 就是  ```a=a+1```


### like 還是關鍵字搜尋
```sql
 SELECT content FROM imychunk where content like '%Artificial Intelligence%';
 ```
 
 ### 語意搜尋只有 ```Vector Store``` 做得到
 ### 如果有一份文件很大，如何切chunk?
 1. 不管原來文件格式，一定要先轉成純文字
 2. Chunking 策略要考慮原來知識的結構
 (1)例如 Q&A 結構，就一組Q&A一個data chunk 切
 (2)法律條文 條、項、款、目做為一個chunk
 (3)上下文關係(段落分明) 就以段為單位  
 (4)上下文關係(段落不分明)，固定 chunk size， 但每個chunk 與 前一個chunk 有overlapping， such as 1/2
 (5)其他 semantic-based
 