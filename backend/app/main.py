from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import pytz
import pandas as pd
from .db import insert_data, select_data
import io

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

@app.get("/down/")
async def down_data():
    data = pd.DataFrame(select_data())
    response = StreamingResponse(io.StringIO(data.to_csv(index=False)), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    return response
    