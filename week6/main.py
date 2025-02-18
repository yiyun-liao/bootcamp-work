from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from starlette.status import HTTP_303_SEE_OTHER
from fastapi.templating import Jinja2Templates
import mysql.connector


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")
templates = Jinja2Templates(directory="week6/templates")

def get_db_connection():
    return mysql.connector.connect(
        user="root",
        password="12345678",
        host="localhost",
        database="website"
    )

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html",{
        "request": request,
        "pageTitle": "week6 member system",
        "title": "歡迎光臨，請註冊登入系統",
    })

@app.post("/signup")
async def signup(request:Request, signup_name:str = Form(...), signup_username:str = Form(...), signup_password:str = Form(...)):
    print(f"註冊帳號：姓名： {signup_name}, 帳號：{signup_username}, 密碼：{signup_password}")

    # 連線
    db=get_db_connection()
    cursor=db.cursor(dictionary=True)

    # 檢查帳號是否已經存在
    cursor.execute("SELECT * FROM member WHERE username=%s", (signup_username,))
    user_is_exited = cursor.fetchone()

    # 存在
    if user_is_exited:
        print(f"註冊失敗 {user_is_exited['username'] } 已經存在")
        db.close()
        return RedirectResponse(url="/error?message=帳號或密碼不正確，請重新登入", status_code=HTTP_303_SEE_OTHER)
    
    # 不存在
    cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)",(signup_name, signup_username, signup_password))
    db.commit()
    db.close()
    print(f"註冊成功 {signup_username} 已加入資料庫")
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)




@app.post("/signin")
async def login(request: Request, signin_username: str = Form(...), signin_password: str = Form(...)):
    print(signin_username, signin_password) 

    db=get_db_connection()
    cursor=db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM member WHERE username=%s and password =%s", (signin_username, signin_password))
    user_is_member=cursor.fetchone()
    if user_is_member is None:
        print("登入失敗")
        db.close()
        return RedirectResponse(url="/error?message=帳號或密碼不正確，請重新登入",status_code=HTTP_303_SEE_OTHER)
    else:
        db.commit()
        db.close()
        print("登入成功", user_is_member)
        request.session["SIGNIN"] = True
        return RedirectResponse("/member", status_code=HTTP_303_SEE_OTHER)


@app.get("/member")
def member(request: Request, username: str = "您好"):
    if not request.session.get("SIGNIN"):
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
