from fastapi import FastAPI, Form, Request, Query
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from starlette.status import HTTP_303_SEE_OTHER
from fastapi.templating import Jinja2Templates
import mysql.connector
from typing import Annotated, Union
from dotenv import load_dotenv
import os


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
PASSWORD = os.getenv("PASSWORD")


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
templates = Jinja2Templates(directory="week7/templates")


def get_db_connection():
    return mysql.connector.connect(
        user="root",
        password=PASSWORD,
        host="localhost",
        database="website"
    )

@app.get("/")
def index(request: Request):
    if request.session.get("SIGNIN") is True:
        return RedirectResponse(url="/member", status_code=HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("index.html",{
        "request": request,
        "pageTitle": "week7 前後端分離",
        "title": "歡迎光臨，請註冊登入系統",
    })

@app.post("/signup")
async def signup(request:Request, signup_name:str = Form(...), signup_username:str = Form(...), signup_password:str = Form(...)):
    print(f"註冊帳號：姓名： {signup_name}, 帳號：{signup_username}, 密碼：{signup_password}")

    # 連線
    db=get_db_connection()
    cursor=db.cursor(dictionary=True)

    # 檢查帳號是否已經存在
    cursor.execute("SELECT * FROM member WHERE username=%s;", (signup_username,))
    user_is_exited = cursor.fetchone()

    # 存在
    if user_is_exited:
        print(f"註冊失敗 {user_is_exited['username'] } 已經存在")
        db.close()
        return RedirectResponse(url="/error?message=帳號或密碼不正確，請重新登入註冊", status_code=HTTP_303_SEE_OTHER)
    
    # 不存在
    cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s);",(signup_name, signup_username, signup_password))
    db.commit()
    db.close()
    print(f"註冊成功 {signup_username} 已加入資料庫")
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)




@app.post("/signin")
async def login(request: Request, signin_username: str = Form(...), signin_password: str = Form(...)):
    print(signin_username, signin_password) 

    db=get_db_connection()
    cursor=db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM member WHERE username=%s and password =%s;", (signin_username, signin_password))
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
        request.session["member_id"] = user_is_member['id']
        request.session['username'] = user_is_member['username']
        request.session['name'] = user_is_member['name']
        return RedirectResponse("/member", status_code=HTTP_303_SEE_OTHER)


@app.get("/member")
def member(request: Request):
    if not request.session.get("SIGNIN"):
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    
    print("當前 session 資料:", request.session)

    messages = get_messages()

    name=request.session.get("name")
    return templates.TemplateResponse("member.html", {
        "request": request,
        "pageTitle": "week7 前後端分離",
        "title": "歡迎光臨，這是會員頁",
        "username": name,
        "messages": messages
        })

@app.get("/error")
def error(request: Request, message: str = "Login failed"):
    return templates.TemplateResponse("error.html", {
        "request": request,
        "pageTitle": "week7 前後端分離",
        "title": "失敗頁面",
        "subtitle": message
    })

@app.get("/signout")
def signout(request:Request):
    request.session.clear() 
    # print("當前 session 資料:", request.session)
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)

app.mount("/static", StaticFiles(directory="week7/static"), name="static")

@app.post("/createMessage")
def create_message(request:Request, create_message_content: str = Form(...)):
    member_id = request.session.get("member_id")
    print(f"{member_id} 傳送了 {create_message_content}")

    create_message=get_db_connection()
    create_message_cursor=create_message.cursor(dictionary=True)

    create_message_cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s);", (member_id, create_message_content))
    create_message.commit()
    create_message.close()    
    return RedirectResponse(url="/member", status_code=HTTP_303_SEE_OTHER)
 

def get_messages():
    get_message = get_db_connection()
    get_message_cursor = get_message.cursor(dictionary=True)
    get_message_cursor.execute("SELECT message.id, member.id AS member_id, member.name, message.content FROM message INNER JOIN member ON message.member_id=member.id ORDER BY message.id DESC ;")
    messages=get_message_cursor.fetchall()
    get_message.commit()
    get_message.close()
    # print(messages)
    return messages
        
@app.delete("/deleteMessage/{message_id}")
async def delete_message(request:Request, message_id: int):
    if not request.session.get('SIGNIN'):
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    print(message_id)
    db=get_db_connection()
    cursor=db.cursor(dictionary=True)
    cursor.execute("DELETE FROM message where id=%s",(message_id,))
    print("成功刪除")
    db.commit()
    db.close()
    return RedirectResponse(url="/member", status_code=HTTP_303_SEE_OTHER)

@app.get("/api/member")
async def search_member_username(request:Request, username: Union[int, str] = Query(...)):    
    with get_db_connection() as db:
        with db.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM member WHERE username=%s;", (username, ))
            username_is_exit=cursor.fetchone()
            if username_is_exit is None:
                print(f"查無使用者: {username}")
                return JSONResponse({"data": None})
            else:
                result = {
                    "data":{
                        "id": username_is_exit["id"],
                        "name":username_is_exit["name"],
                        "username":username_is_exit["username"]
                    }
                }
                print (result)
                return JSONResponse(content=result, status_code=200)
            
@app.patch("/api/member")
async def update_member_username(request:Request):
    new_name_data= await request.json()
    print(new_name_data)
    new_name = new_name_data.get("name","")
    name = request.session.get("name")
    member_id = request.session.get("member_id")
    with get_db_connection() as db:
        with db.cursor(dictionary=True) as cursor:
            cursor.execute("UPDATE member SET name=%s WHERE id=%s;", (new_name, member_id))
            db.commit()

            # 檢查更新是否成功
            if cursor.rowcount > 0:
                print(f"{member_id} 更新成功: {name} to {new_name}" )
                return {"ok": True}
            else:
                print(f"更新失敗")
                return {"error": True}



