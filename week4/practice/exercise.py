from fastapi import FastAPI, Query, Path
from typing import Annotated

app = FastAPI() #產生 FastAPI 的物件
# terminal: uvicorn week4.practice.exercise:app --reload

# --------------kick off---------------------------------------------
# 處理路由設定，處理路徑 /
@app.get("/")
def index():
    return "Hello FastAPI"
# 處理路由設定，處理路徑 /data
@app.get("/data")
def index():
    return {"data":[2,3,1]}

# 讓前端可以透過網址輸入一個數字，後端把輸入的數字作平方，在回應給前端
@app.get("/square/10")
def square1():
    return{"result": 10*10}
# 使用路徑參數，處理有相同前綴字 /square/ 的路徑
@app.get("/square/{number}")
def square2(number):
    number=int(number) #預設為字串型態，轉換為數字
    return{"result": number*number}

# --------------structure------------------------------------------
# 處理路徑 /hello?name=名字
# @app.get("/hello")
# def hello(name):
#     message = "哈囉，"+name
#     return {"message":message}
# http://127.0.0.1:8000/hello?name=%E9%BD%8A%E9%BD%8A => 齊齊
# http://127.0.0.1:8000/hello 這個路由沒有 name 參數，會導致 FastAPI 無法正確解析請求，因為函式 hello(name) 需要 name 參數，但路由沒有提供。

# 同時支援 /hello 和 /hello/{name}
@app.get("/hello")
@app.get("/hello/{name}")
def hello(name: str = "訪客"):
    message = "哈囉，" + name
    return {"message": message}

# 處理路徑 /multiply?n1=數字＆n2=數字
@app.get("/multiply")
def multiply1(n1, n2):
    n1=int(n1)
    n2=int(n2)
    result=n1*n2
    return {"result":result}
# http://127.0.0.1:8000/multiply?n1=5&n2=10 => 50


# --------------annotated, path, query---------------------------------------------
#路徑參數
# 前端： http://127.0.0.1:8000/square/9
@app.get("/square/{number}")
def square3(number:Annotated[int,Path(gt=3,lt=10)]):
    number=int(number)
    return{"result": number*number}

# 要求字串
# 前端： http://127.0.0.1:8000/multiply?n1=10&n2=3
@app.get("/multiply")
def multiply2(
  n1: Annotated[int,Query(ge=0, le=10)],
  n2: Annotated[int,Query(ge=0, le=10)]
):
    n1=int(n1)
    n2=int(n2)
    result=n1*n2
    return {"result": result}

# 前端： http://127.0.0.1:8000/echo/mary
@app.get("/echo/{name}")
def echo(name: Annotated[str,Path(min_length=2, max_length=30)]):
    return {"message":"Hello "+name}

# --------------response---------------------------------------------
# JSONResponse fun1
@app.get("/")
def index1():
    return {"data":[1,2,3]}

# JSONResponse fun2
from fastapi.responses import JSONResponse
@app.get("/")
def index2():
    return JSONResponse({"data":[1,2,3]})

#HTMLResponse
from fastapi.responses import HTMLResponse
@app.get("/")
def index3():
    return HTMLResponse("""
        <h3>網頁標題</h3>
        <div>簡單的內容</div>
    """)

#FileResponse
from fastapi.responses import FileResponse
@app.get("/")
def index4():
    return FileResponse("index.html")
@app.get("/logo")
def index5():
    return FileResponse("logo.png")

#PlainTextResponse
from fastapi.responses import PlainTextResponse
@app.get("/")
def index6():
    return PlainTextResponse("就是文字而已")
@app.get("/")
def index7():
    return PlainTextResponse("""
        <h3>仍然是純文字</h3>
        <div>不會被當成網頁標籤處理</div>
    """)

#RedirectResponse
from fastapi.responses import RedirectResponse
@app.get("/")
def index8():
    return {"data":[1,2,3]}
@app.get("/member")
def index9():
    return RedirectResponse("/")