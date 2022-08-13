from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
import pytz
from .db import insert_data

class Data(BaseModel):
    use : list
    weather : str

db = []

app = FastAPI()

def now_date_time():
    tz = pytz.timezone('Asia/Seoul')
    return datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

@app.get("/")
def root():
    return "welcome"

@app.get("/info/")
async def get_info():
    ls = []
    for i in db:
        ls.append({'date':i['date'], 'weather':i['weather'], 'use':i['use']})
    return ls

@app.post("/info/")
async def create_info(data:Data):
    df = data.dict()
    df['date'] = now_date_time()
    db.append(df)
    query_data = []
    query_data.append(df['date'])
    query_data.append(df['weather'])
    query_data.extend(df['use'])
    insert_data(tuple(query_data))
    return db[-1]