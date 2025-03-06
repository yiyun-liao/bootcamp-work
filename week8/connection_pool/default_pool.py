from fastapi import FastAPI, Form, Request, Query, Response
from mysql.connector import pooling
from dotenv import load_dotenv
import os
import time


load_dotenv()
PASSWORD = os.getenv("PASSWORD")


app = FastAPI()

pool = pooling.MySQLConnectionPool(
    user="root",
    password=PASSWORD,
    host="localhost",
    database="website",
    pool_name="mypool", 
    pool_size=5)

def connection():
    start_time = time.perf_counter()
    db=pool.get_connection()
    cursor=db.cursor(dictionary=True)
    cursor.execute("SELECT VERSION()")
    version = cursor.fetchone()
    end_time = time.perf_counter()
    connection_time = (end_time-start_time)*1000
    print(f"{version}, spent {connection_time} ms")
    db.close()

for _ in range(10):
    connection()

