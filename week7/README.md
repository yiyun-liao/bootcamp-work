## Task 1: Build a Member Query API in the back-end
- 紀錄一： db connect 用 with 寫
- 紀錄二：依著作業順序進行的話會沒有前端畫面佐證，所以試著用 PostMan 進行
- 紀錄三：測試時帳號使用 `test04` 會有 int + str 的需求，使用如果一個變數可以是**多種類型**，可以用 `Union`
- 紀錄四：接收前端傳來的資料 `form(...)`, `Query(...)`, `Body(...)`

|方法 | 用途 | 用在哪裡|
|-- | -- | --|
|Form(...) | 接收表單數據 (application/x-www-form-urlencoded) | HTML  提交的資料|
|Query(...) | 接收 URL 參數 (?username=abc) | GET 請求的查詢參數|
|Body(...) | 接收 JSON 格式的請求 (application/json) | API 使用 AJAX 提交的 JSON 資料|

## Task 2: Call Member Query API by fetch function in the front-end
- `JSONResponse` FastAPI 預設使用 JSON 格式回應 ，所以可以直接寫 return json 格式的內容
- `event.preventDefault();` 避免頁面刷新，複習事件冒泡（Event Bubbling） 和 事件捕獲（Event Capturing）
- `${encodeURIComponent(username)}` 維持中文字輸入
- 利用 `searchUsernameResult.querySelector('p').` 往下找 `<p>` 就不用再另外設定 id

## Task 3: Add feature for updating name
- 紀錄一：資料變動狀況的方法：
	- 1, `cursor.rowcount`
	- 2, 把資料拉出來跟原本放入的 new_name 比對是否正確
- 紀錄二：輸入一樣的名字的判斷原本是想說要做在前端直接判斷，但應該可以做在後端做練習，但是目前的 return 只能給兩個選項，所以無法提供到更多的資訊
- 紀錄三：用 postman 要走更新流程時因為需要 cookie(middleware)，所以需要從登入流程走一次，讓 postman 紀錄 cookie
- 紀錄四：`json_data.get("key", default_value)` 用來安全地從字典中取出值，如果鍵不存在則返回指定的默認值。`json_data["key"]` 用來直接從字典中取出值，但如果鍵不存在會引發 `KeyError`。


- 紀錄一：發現存在 session 中的資料會一直維持在一開始登入的內容，雖然當下更改名字時有更新到 h2 的標題，但是 refresh 後頁面主要的 title 還是會變成一開始登入時所記錄的內容，故更改名字時也要儲存 session 中的紀錄。而 message 的資料在每次 refresh 時是重新跟 MySQL 取，所以會有最新的名字
- 紀錄二：這段 message 一直無法證成更新，後來才想到要判斷的是舊的 greetingName.textContent (`${new_username}，歡迎登入系統` ) 所以將這段移到最下面就成功了
-
```javascript
    if (data.error){
        console.log("error")
        updateUsernameResult.querySelector('p').textContent="更新失敗";
    }else if (data.ok){
        console.log("success")
        updateUsernameResult.querySelector('p').textContent="更新成功";
        messageListName.forEach(item => {
            if (item.textContent === greetingName.textContent.split("，")[0]){
                item.textContent= new_username;
                console.log("change", new_username)
            }else{
                console.log("fail", new_username)
            }
        })
    greetingName.textContent = `${new_username}，歡迎登入系統`;}
```