from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from starlette.status import HTTP_303_SEE_OTHER
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")
templates = Jinja2Templates(directory="week4/templates")

# import time
# @app.middleware("http")
# async def check_signed_in_status(request: Request, call_next):
#     print('>>>', request.method)
#     start_time = time.perf_counter()
#     response = await call_next(request)
#     process_time = time.perf_counter() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response


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
        return RedirectResponse(url="/error?message=請完整輸入帳號密碼", status_code=HTTP_303_SEE_OTHER)
    if username != "test":
        return RedirectResponse(url="/error?message=帳號不存在，請重新登入", status_code=HTTP_303_SEE_OTHER)
    if password != "test":
        return RedirectResponse(url="/error?message=密碼錯誤，請重新輸入", status_code=HTTP_303_SEE_OTHER)
    else:
        request.session["SIGNED-IN"] = True
        return RedirectResponse(url="/member", status_code=HTTP_303_SEE_OTHER)


@app.get("/member")
def member(request: Request):
    if not request.session.get("SIGNED-IN"):
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("member.html", {
        "request": request,
        "title": "歡迎光臨，這是會員頁",
        "subtitle": "恭喜你，成功登入系統"
        })

@app.get("/error")
def error(request: Request, message: str = "Login failed"):
    return templates.TemplateResponse("error.html", {
        "request": request,
        "title": "失敗頁面",
        "subtitle": message
    })

@app.get("/signout")
def signout(request:Request):
    request.session.clear() 
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)

app.mount("/static", StaticFiles(directory="week4/static"), name="static")
