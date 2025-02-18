from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from starlette.status import HTTP_303_SEE_OTHER
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")
templates = Jinja2Templates(directory="week6/templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html",{
        "request": request,
        "pageTitle": "week6 member system",
        "title": "歡迎光臨，請註冊登入系統",
    })

@app.get("/signup")
async def signup(request:Request, signup_name:str = Form(...), signup_username:str = Form(...), signup_password:str = Form(...)):
    print(signup_name, signup_username, signup_password)
    


@app.post("/login")
async def login(request: Request, login_username: str = Form(...), login_password: str = Form(...)):
    print(login_username, login_password) #"test" , "test"
    if not login_username or not login_password:
        return RedirectResponse(url="/error?message=請完整輸入帳號密碼", status_code=HTTP_303_SEE_OTHER)
    if login_username != "test":
        return RedirectResponse(url="/error?message=帳號不存在，請重新登入", status_code=HTTP_303_SEE_OTHER)
    if login_password != "test":
        return RedirectResponse(url="/error?message=密碼錯誤，請重新輸入", status_code=HTTP_303_SEE_OTHER)
    else:
        request.session["LOG-IN"] = True
        return RedirectResponse(url="/member", status_code=HTTP_303_SEE_OTHER)


@app.get("/member")
def member(request: Request, username: str = "您好"):
    if not request.session.get("LOG-IN"):
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("member.html", {
        "request": request,
        "pageTitle": "week6 member system",
        "title": "歡迎光臨，這是會員頁",
        "username": username
        })

@app.get("/error")
def error(request: Request, message: str = "Login failed"):
    return templates.TemplateResponse("error.html", {
        "request": request,
        "pageTitle": "week6 member system",
        "title": "失敗頁面",
        "subtitle": message
    })

@app.get("/signout")
def signout(request:Request):
    request.session.clear() 
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)

app.mount("/static", StaticFiles(directory="week6/static"), name="static")
