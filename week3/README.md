## Task1 python and api
- 紀錄一：卡在 ssl 憑證問題，試了更新 certifi, uninstall and install python 都沒有成功，先利用手動解除的方式繼續進行作業。
- 紀錄二：因為要讀入兩個 url ，所以將 `with request.urlopen(src) as response:` 寫進函式中，方便複用
- 紀錄三：因為文件中有中文，所以用 `utf-8` 編碼，`with open("data.txt", "w", encoding="utf-8") as file:`
- 紀錄四：編寫文件：
	- `with open("file", "mode") as obj`開啟一個文件並作為文件物件返回
	- `csv.writer(*csvfile*,&nbsp;*dialect='excel'*,&nbsp;**fmtparams)`
	- `writer.writerow(row)` 將單列（row）的資料寫入 CSV 檔案。
	- 如果需要有表頭就將該行 `writer.writerow(["SpotTitle", "District", "Longitude", "Latitude", "ImageURL"])`寫在回圈之外，如果不需要，就直接在回圈內寫就好
	- setdefault(keyname, value), get(keyname, value) 差別在哪
	- `f"str"` F-string allows you to format selected parts of a string.
	- `split()` Split a string into a list where each word is a list item
	- *條件表達式（conditional expression）*，也叫做三元運算子（ternary operator）
	- `item()` 回傳 dict 中的 key-value

- 紀錄五：什麼時候要用 `[]`, `{}`

特性 | 列表 [] | 字典 {}
-- | -- | --
儲存結構 | 單一資料的集合 | 鍵值對（key-value pairs）
順序 | 有序 | 無序（Python 3.7+ 順序保留）
重複性 | 可以有重複值 | 鍵唯一，值可重複
查找速度 | 按索引查找，速度快 | 鍵查找速度非常快
使用場景 | 需要有序列表 | 需要快速查找或結構化資料

## Task03 JS and api
- `Array.prototype.filter()`: 建立一個新陣列，其元素為通過指定條件的原陣列元素。
- `Array.prototype.slice()`: 回傳一部分的陣列作為新陣列。
- `Array.prototype.map()` 建立新的 array
- `String.prototype.split()`  將字串分割成一個小區的子字串列表
- **Fetch API**
- **async/await**
- **Promise**
- 
  Promise 是基礎，可以處理非同步邏輯，但容易出現回調嵌套問題。
  Async/Await 用於簡化基於 Promise 的非同步程式碼，讓程式碼看起來更像同步操作。
  Fetch API 是用於網絡請求的內建工具，返回 Promise。

特性 | Promise | Async/Await
-- | -- | --
語法 | 使用 .then() 和 .catch() 處理結果。 | 更接近同步程式碼風格，使用 try/catch。
可讀性 | 回調嵌套較多，對於複雜邏輯可讀性較差。 | 簡化非同步流程，可讀性更強。
錯誤處理 | 使用 .catch() 捕捉錯誤。 | 使用 try/catch 捕捉錯誤。
使用場景 | 簡單的非同步操作，例如單次請求。 | 複雜邏輯或多次請求的情況。

## Task04 增加行為
- 調整一 `cloneNode(true)`
	- 使用 creatHTML 如果是 `<li>`, 那裡面即使沒有跟著 api 而有改變的如星星 icon 都需要 create ，但其實可以用複製的方式來複製 `<li>` 就能確保樣式和結構
- 調整二 解決既有空白的 li 問題
	- css 中使用 `display: none` 來隱藏，只有觸發時才會顯示 `<li>`
	- 同步 html 中原本有寫了十個 <li> 因為是用複製的方式，所以把多餘的九個移除 => 好像不能這樣刪，因為用 `display: none` 這些 `<li>` 還是存在，會影響到排版，如果只保留一個，那原本計算第一個第六個會比較大的設計就會在這邊出現問題
- 調整三 大圖原本的十張跟後來長出來的分開寫
	- 原本的寫法是讓大圖的渲染是跟加十張的渲染邏輯放在一起，但一直遇到會顯示空白十張的問題。
	- 覺得在第一次開啟頁面時就要完成大圖跟小圖的顯示，不應該是用計算的，所以把 task3 的大圖顯示邏輯加回來
	- 所以是：`fetch()` 時直接完成三小張、十大張的渲染
	- 點擊按鈕時走 `renderBigBoxes()` 去增加十張
- 調整四 不同 rwd 下介面排版不同
	- screen > 1200px `.big-boxes li:nth-child(5n+1) {grid-column: span 2;}`
	- 1200px > screen > 600 用 js 寫
		- function 獨立運行，並且在 fetch(), 跟每次點擊時會重新計算
		-
        ```javascript
        if(window.matchMedia("(min-width: 600px) and (max-width: 1200px)").matches){
        bigBoxes.forEach(box => {
            box.style.gridColumn = 'span 1';
        });
        if(currentIndex % 4 !== 0){
            bigBoxes[currentIndex-1].style.gridColumn = 'span 2';
            bigBoxes[currentIndex-2].style.gridColumn = 'span 2';
        }
        }
        ```
