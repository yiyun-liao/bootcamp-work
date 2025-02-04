from fastapi import FastAPI, Query, Path
from typing import Annotated
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI() #產生 FastAPI 的物件

# --------------method---------------------------------------------
# 處理 GET 方法的路徑 /test
@app.get("/test")
def testGet():
    return {"data":10, "method":"GET"}
#處理 POST 方法的路徑 /test
@app.post("/test")
def testPost():
    return {"ok":True, "method":"POST"}

from fastapi.routing import APIRoute
for route in app.routes:
    print(route.path, route.methods)

# --------------前後端連接---------------------------------------------
@app.get("/square")
def square(num:Annotated[int,None]):
    result= num*num
    return {"data":result}

@app.get("/multiply")
def multiply(n1:Annotated[int,None], n2:Annotated[int,None]):
    result = n1 * n2
    return{"data":result}

@app.get("/member")
def member():
    return RedirectResponse("/")

#連回首頁及取得對應圖片
app.mount("/",StaticFiles(directory="week4/practice/public", html=True))
