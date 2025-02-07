from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.status import HTTP_303_SEE_OTHER
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="week4/templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html",{
        "request": request,
        "title": "歡迎光臨，請輸入帳號密碼",
        "subtitle": "登入系統"
    })

@app.post("/signin")
async def signin(request: Request, username: str = Form(...), password: str = Form(...)):
    print(username, password) #"test" , "test"
    if not username or not password:
        return RedirectResponse(url="/error?msg=請完整輸入帳號密碼", status_code=HTTP_303_SEE_OTHER)
    if username != "test":
        return RedirectResponse(url="/error?msg=帳號不存在，請重新登入", status_code=HTTP_303_SEE_OTHER)
    if password != "test":
        return RedirectResponse(url="/error?msg=密碼錯誤，請重新輸入", status_code=HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse(url="/member", status_code=HTTP_303_SEE_OTHER)


@app.get("/member")
def member(request: Request):
    return templates.TemplateResponse("member.html", {
        "request": request,
        "title": "歡迎光臨，這是會員頁",
        "subtitle": "恭喜你，成功登入系統"
        })

@app.get("/error")
def error(request: Request, msg: str = "Login failed"):
    return templates.TemplateResponse("error.html", {
        "request": request,
        "title": "失敗頁面",
        "subtitle": msg
    })

app.mount("/static", StaticFiles(directory="week4/static"), name="static")


# import time
# from fastapi.middleware import Middleware
# from starlette.middleware.base import BaseHTTPMiddleware

# class CustomHeaderMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request, call_next):
#         print('>>>', request.method)
#         # start_time = time.time()
#         response = await call_next(request)
#         # process_time = time.time() - start_time
#         # response.headers["X-Process-Time"] = str(process_time)
#         return response
    
# middleware = [
#     Middleware(CustomHeaderMiddleware)
# ]

# app = FastAPI(middleware=middleware)