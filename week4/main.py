from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# 處理登入請求
@app.post("/signin")
async def signin(request:Request):
    json_data = await request.json()
    username = json_data.get("username","")
    password = json_data.get("password","")

    if not username or not password:
        return {"error": "Please enter username and password"}
    
    if username == "test" and password == "test":
        return {"message": "Login successful"}
    
    return {"error": "Username or password is not correct"}


# 成功頁面
# @app.get("/member")
# async def member():
#     return "Login successful! Welcome to the member page."

# 錯誤頁面
# @app.get("/error")
# async def error(message: str):
#     return f"Login failed: {message}"

# from fastapi.routing import APIRoute
# for route in app.routes:
#     print(route.path, route.methods)

app.mount("/", StaticFiles(directory="week4/service", html=True), name="static")
