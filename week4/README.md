## task01
**new**
- `autocomplete=` 帳號密碼時由瀏覽器提供密碼自動填充的建議
- `addEventListener` type: https://developer.mozilla.org/en-US/docs/Web/Events `'submit'`
- 網頁的生命週期 `DOMContentLoaded`
- `request.json()` vs. `response.json()` 的區別

**review**
- form elements `<form>`, `input`, `label`, `select`
   - 之前看不懂 method, action 現在重頭看比較理解是什麼意思
   - `form action="test"` = path, `http://127.0.0.1/test?name=username`
   - `label for=""` 動應到 `input id=""`
   - `input name="test"` = query string, `http://127.0.0.1/action?name=test` 

## task02
- 紀錄一，在 /signin 中用 RedirectResponse 回傳了一個 HTML 頁面，但前端的 <code>fetch</code> 嘗試解析成 JSON，導致錯誤。所以方法一：前端不強制解析 JSON 而是先檢查回傳格式。方法二：後端回傳 JSON 讓前端處理跳轉。
    - 前端送出的為：
  ```javascript
  console.log(formData.toString()); //username=test&amp;password=test
  ```

    - 前端接收後解析的為 JSON：
  ```javascript
  const data = await response.json();
  ```

    - 方法一：
        - <code>response.headers.get("content-type")</code> 會回傳回應的 <code>Content-Type</code>，例如：
        - <code>application/json</code> → JSON 格式
        - <code>text/html</code> → HTML 頁面
        - <code>contentType.includes("application/json")</code>：
        - 如果是 JSON（例如 <code>"application/json; charset=utf-8"</code>）→ 執行 JSON 處理
        - 如果不是（例如 <code>"text/html"</code>）→ 進入 <code>else</code>，執行頁面重導向
  ```javascript
    async function signin() {
        const formData = new FormData();
        formData.append("username", document.getElementById("username").value);
        formData.append("password", document.getElementById("password").value);

    try {
        const response = await fetch("/signin", {
            method: "POST",
            body: formData, 
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // 檢查 Content-Type 是否為 JSON
        const contentType = response.headers.get("content-type");
        if (contentType &amp;&amp; contentType.includes("application/json")) {
            const data = await response.json();
            console.log(data);
        } else {
            console.log("Redirecting to:", response.url);
            window.location.href = response.url;  // 直接導向 HTML 頁面
        }
    } catch (error) {
        console.error("Error", error);
    }
    }
  ```

    - 方法二：用 JSONResponse 回應，在前端處理
    -
  ```javascript
    async function signin() {
        const formData = new FormData();
        formData.append("username", document.getElementById("username").value);
        formData.append("password", document.getElementById("password").value);
    
        try {
            const response = await fetch("/signin", {
                method: "POST",
                body: formData, 
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            if (data.redirect) {
                window.location.href = data.redirect;
            }
        } catch (error) {
            console.error("Error", error);
        }
    }
  ```
    -
  ```python
     from fastapi import FastAPI, Form
     from fastapi.responses import JSONResponse

    app = FastAPI()

    @app.post("/signin")
    async def signin(username: str = Form(...), password: str = Form(...)):
        if username == "test" and password == "test":
            return JSONResponse(content={"redirect": "/member.html"}, status_code=200)
        else:
            return JSONResponse(content={"redirect": "/error.html"}, status_code=200)

  ```
- 紀錄二，form 本身就可以用 `action`, `name` 帶 api, query string ，不需要再寫 js ，要寫 js 是要對資料進行編輯才有需要。整個過程中，用了 application/json , form data 寫 😅
**new**
- `request.json()` vs. `response.json()` 的區別
- 前後端應用
   - 前端 Content-Type
| Content-Type | 用途 |
| -- | --|
| application/json | 代表 JSON 格式的資料（常用於 API）|
| application/x-www-form-urlencoded | 傳送表單資料（傳統 form 提交方式）|
| multipart/form-data | 上傳檔案時使用|
| text/plain | 純文字|

   - 後端解析，當後端接收為 `request: Request`
|解析 | 用途|
|-- | --|
|await request.json() | 請求體（Body）解析 JSON 格式的請求內容。|
|await request.form() | 表單數據（Form） 解析 application/x-www-form-urlencoded 或 multipart/form-data。|
|request.query_params | 查詢參數（Query Params）取得 URL 查詢參數。|
|request.headers | 請求標頭（Headers） 讀取請求標頭資訊。|

   - 前端發送的內容 <code>URLSearchParams</code> vs. <code>FormData()</code> vs. <code>JSON.stringify()</code>

|用途 | URLSearchParams | FormData() | JSON.stringify()|
|-- | -- | -- | --|
|適用格式 | application/x-www-form-urlencoded | multipart/form-data | application/json|
|適合情境 | 一般表單（登入、註冊） | 上傳檔案 | API 傳 JSON|
|是否支援檔案 | ❌ 不支援 | ✅ 支援 | ❌ 不支援|
|是否適合 AJAX API | ❌ 不推薦 | ❌ 不推薦 | ✅ 推薦|

   - 前端發送的內容 <code>fromData()</code>
      - 在 JavaScript 中，FormData() 是一種方便處理表單數據的物件，特別適合處理 動態表單 或 需要上傳檔案的請求。但不是所有表單提交都一定要使用 FormData()，是否需要它取決於 表單的格式 (Content-Type) 和 傳送方式。
      - <code>FormData()</code> 允許動態新增表單字段，適用於 JavaScript 控制的表單提交。

|情境 | 使用 FormData() | 不用 FormData()|
|-- | -- | --|
|上傳檔案 | ✅ 需要（multipart/form-data） | ❌ JSON.stringify() 無法處理 File|
|動態表單欄位（數量不固定） | ✅ 適合（可動態 append 欄位） | ❌ JSON.stringify() 需要手動組合物件|
|普通表單（登入、註冊） | ❌ 不需要（用 URLSearchParams） | ✅ application/x-www-form-urlencoded|
|API 傳 JSON 資料 | ❌ （用 JSON.stringify() 更適合） | ✅ Content-Type: application/json|

   - 需要上傳檔案 → 用 <code>FormData()</code>
   - 動態新增表單欄位 → 用 <code>FormData()</code>
   - 傳送純 JSON（API → 用 <code>JSON.stringify()</code>
   - 普通 HTML 表單提交 → 用 <code>URLSearchParams()</code> 或 <code>application/x-www-form-urlencoded</code>
 
**review**
- 事件冒泡（Event Bubbling）和事件捕獲（Event Capturing）`preventDefault()`

## task03
- 虛擬環境建置：要安裝的東西越來越多，花了一點時間處理虛擬環境
### Jinja2
- `Annotated` vs. 一般 Type Hinting（對比表）

| 比較項目 | 普通 Type Hinting | Annotated |
| ---- | ---- | ---- |
| **定義方式** | `msg: str = "text"` | `msg: Annotated[str, Query(...)]` |
| **作用** | 只作為類型提示 | 可額外添加驗證、元數據等 |
| **FastAPI 兼容** | 只能標註類型，FastAPI 需手動檢查 | FastAPI 會自動驗證 |
| **影響運行時行為** | ❌ 不影響 | ✅ 可能影響 |
| **支援的元數據** | ❌ 沒有額外資訊 | ✅ `Query()`、`Depends()`、`Path()`、`Body()` 等 |
| **適用場景** | 一般函式參數 | FastAPI 參數驗證、依賴注入 |
- 類型提示 `Type Hinting`

| 用法 | 範例 | 說明 |
| ---- | ---- | ---- |
| FastAPI 路由參數 | `def read_item(q: str = "default")` | `q` 是字串，預設 `"default"` |
| 一般函式參數 | `def greet(name: str, age: int) -> str` | `name` 是字串，`age` 是整數，回傳 `str` |
| 類別 (`dataclass`) | `@dataclass class User: username: str` | 屬性有明確類型 |
| 類別 (`pydantic`) | `class User(BaseModel): age: int` | FastAPI 常用 |
| `Union` | `Union[int, str]` | 允許多種類型 |
| `Optional` | `Optional[str]` | 允許 `None` |
| `List`、`Dict` | `List[str]`、`Dict[str, int]` | 限制集合類型 |
| 類別方法 | `def greet(self) -> str` | 顯示回傳類型 |

### middleware
- Starlette 中用來向應用程式添加的方式。中介軟體是處理請求和回應的處理程式，位於請求進入應用程式和回應返回用戶之間。它可以用來執行一些通用的功能，例如日誌紀錄、錯誤處理、會話管理、跨來源資源共享（CORS）、安全檢查等。