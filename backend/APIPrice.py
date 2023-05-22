from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
#import sqlite3
from contextlib import asynccontextmanager
import time

from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb

connection = MySQLdb.connect(
  host= os.getenv("HOST"),
  user=os.getenv("USERNAME"),
  passwd= os.getenv("PASSWORD"),
  db= os.getenv("DATABASE"),
  autocommit = True,
  ssl_mode = "VERIFY_IDENTITY",
  ssl = {
    "ca": "/etc/ssl/certs/ca-certificates.crt"
  }
)

try:
    cur = connection.cursor()
except:
    print("error")
    os.exit()

origins = [
    "localhost:3000"
]

class Item(BaseModel):
    link2: str
    email: str


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
async def _(model: Item):
    cur.execute("INSERT INTO Products (link, email, prevPrice) VALUES (%s, %s, -1)", (model.link2, model.email))

@app.post("/delete/", status_code=204)
async def _(model: Item):
    cur.execute("DELETE FROM Products WHERE link=%s AND email=%s", (model.link2, model.email))

