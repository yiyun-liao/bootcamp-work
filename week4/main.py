from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

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

app = FastAPI()

# 處理登入請求 使用  Form Data
@app.post("/signin")
async def signin(username: str = Form(...), password: str = Form(...)):
    print(username, password) #"test" , "test"
    if username == "test" and password == "test":
        return JSONResponse(content={"redirect": "/member.html"}, status_code=200)
    else:
        return JSONResponse(content={"redirect": "/error.html"}, status_code=200)

app.mount("/", StaticFiles(directory="week4/service", html=True), name="static")
