from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.status import HTTP_303_SEE_OTHER

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

@app.post("/signin")
async def signin(username: str = Form(...), password: str = Form(...)):
    print(username, password) #"test" , "test"
    if not username or not password:
        return RedirectResponse(url="/error?message=Please enter username and password", status_code=HTTP_303_SEE_OTHER)
    if username == "test" and password == "test":
        return RedirectResponse(url="/member", status_code=HTTP_303_SEE_OTHER)
    return RedirectResponse(url="/error?message=Username or password is not correct", status_code=HTTP_303_SEE_OTHER)

@app.get("/member")
def member():
    return FileResponse("week4/service/member.html")

@app.get("/error")
def errot():
    return FileResponse("week4/service/error.html")


app.mount("/", StaticFiles(directory="week4/service", html=True), name="static")
