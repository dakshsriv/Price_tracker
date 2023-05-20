from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sqlite3
from contextlib import asynccontextmanager
import time

origins = [
    "*"
]



conn = sqlite3.connect("Price.db")
cur=conn.cursor()

def start():
    print("Started")
    while True:
        cur.execute("SELECT * FROM Products")
        lst = cur.fetchall()
        print(lst)
        time.sleep(3)
        

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/", status_code=204)
async def _(link2: str, email: str):
    cur.execute("INSERT INTO Products (link, email, prevPrice) VALUES (?, ?, -1)", (link2, email))
    conn.commit()

@app.delete("/", status_code=204)
async def _(link2: str, email: str):
    cur.execute("DELETE FROM Products WHERE link=? AND email=?", (link2, email))
    conn.commit()

