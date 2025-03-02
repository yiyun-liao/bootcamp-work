import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
PASSWORD = os.getenv("PASSWORD")

def get_db_connection():
    return mysql.connector.connect(
         user="root",
         password=PASSWORD,
         host="localhost",
         database="website",
    )

from fastapi import FastAPI, Body, Request
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# 建立後端 Restful APIs
@app.post("/api/message")
def create_message(body :dict = Body(...)):
    # 預期前端透過 request body 請求文本傳遞 {"author":"姓名", "content":"內容"}
    content = body.get("content", "")
    print(content)
    # 連線到資料庫，新增到資料表中
    with get_db_connection() as db:
        with db.cursor(dictionary=True) as cursor:
            # cursor.execute("INSERT INTO message (author, content) VALUES (%s, %s)",(author, content))
            # 因為用目前有的表測試，所以調整一下格式
            cursor.execute("INSERT INTO message (member_id, content) VALUES (1, %s);", (content, ))
            db.commit()
            return JSONResponse(content={"ok":True}, status_code=200)

# # 建立後端 Restful APIs，用 request
# @app.post("/api/message")
# async def create_message(request:Request):
#     body = await request.json()
#     content = body.get("content", "")
#     print(content)
#     # 連線到資料庫，新增到資料表中
#     with get_db_connection() as db:
#         with db.cursor(dictionary=True) as cursor:
#             # cursor.execute("INSERT INTO message (author, content) VALUES (%s, %s)",(author, content))
#             # 因為用目前有的表測試，所以調整一下格式
#             cursor.execute("INSERT INTO message (member_id, content) VALUES (1, %s);", (content, ))
#             db.commit()
#             return JSONResponse(content={"ok":True}, status_code=200)

# 取得所有留言 api
@app.get("/api/message")
async def get_message():
    with get_db_connection() as db:
        with db.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM message")
            data = cursor.fetchall()
            return data
    return JSONResponse(content={"ok":True}, status_code=200)


# 根據 id 刪除留言
@app.delete("/api/message/{id}")
async def delete_message(id:int):
    with get_db_connection() as db:
        with db.cursor(dictionary=True) as cursor:
            cursor.execute("DELETE FROM message WHERE id=%s", (id,))
            db.commit()
            print("成功刪除")
    return JSONResponse(content={"ok":True}, status_code=200)



# 靜態檔案處理，支援前端網頁呈現
app.mount("/",StaticFiles(directory="practice_python/restful_api_practice/public", html=True))
