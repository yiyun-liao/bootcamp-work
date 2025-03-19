## Task 1: Pages
- 使用 week4,5 所做的網頁先將框架做起來，並調整介面

## Task 2: Build a procedure for signing up
- Check if there is any empty input
- Build a procedure for signing up
- 紀錄一：使用了這兩週學的內容，將 Jinja2Templates,  FastAPI, MySQL 放在一起應用。但很多語法都忘記了，要翻筆記喚醒記憶
- 紀錄二：submit 按鈕做 disable 只有在全部都不是空值時才 active
- 紀錄三：目前作業註冊成功還是維持在首頁，原本是想說在 console 或是畫面上做點提示，但查了一下發現作法可能是必須要在網址中帶 string query 然後在前端中去判斷後才能 console，但這跟作業需求不同，所以 debug 上還是先在 python 中印出註冊成功。
- 須研究：
	- 要如何不顯示 password 在檔案中，目前是發 pr 時把密碼改成 12345678，但還是會有忘記的時候
	- 老師影片中的連線是啟動時就建立了資料庫連線，但是在做時有注意到應該是要用時再連線

## Task 3: Build a procedure for signing in
- Check if there is any empty input
- Build a procedure for signing in
- Add user data in session
- 紀錄一：基本上跟 task02 邏輯相同差別是在邏輯上的微調而已
- 紀錄二：增加會員資料到 session 中的操作方式跟當初設定 `request.session["SIGNIN"] = True` 也極為相似

## Task 4: Build a procedure for signing out
- 同 week4 作業

## Task 5: Build a simple message system
- integrates message data to the web page by template engine
- 紀錄一：原本在想要怎麼進行時想到的是像 week3 的作業，將資料傳回前端，用 js 將訊息展現出來。後來在作業上有標示用 template engine 才想到前兩週看的影片中有這部分的練習！
- `{% %}` 和 `{{ }}` 用於嵌入 Python 變數或邏輯指令，讓 HTML 可以動態渲染內容。
- 紀錄二：/member 時要進行拿取 message 資料的 function。在 /createMessage 後也重新導向 /member 這樣也會再次進行拿取 message 資料的 function，就會拿到最新的所有 message

## Task 6: Build a procedure to delete message (Optional)
- 紀錄一：參考了 week3 時的 fetch ，這題這次用 url 去帶資料，應該也可以用 body 帶資料
- 紀錄二：js 中的  `""` `''` `$` 還有反引號。在 JavaScript 中，只有使用反引號時，`${}` 才會被解析為變數的值。但這裡用了單引號，所以 `${messageId}` 和 `${messageMemberId}` 被當成字串，而不是變數。
	- 在 js 中是寫 const response = await fetch(`/deleteMessage/${messageId}/${messageMemberId}`)
	- 在 python 中是寫 @app.delete("/deleteMessage/{message_id}/{message_member_id}")
	- 這是因為 js 中要發送的 path 是前面 function 定義好的變數 `messageId`, `messageMemberId`
	- python 中要使用的是 `async def delete_message()` 中定義好的變數
	- 在各自文件中來自不同的變數，所以寫的不同