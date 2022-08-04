from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

class Data(BaseModel):
    name : str
    num : int

db = []

app = FastAPI()

@app.get("/")
def root():
    return "welcome"

@app.get("/info/")
async def get_info():
    ls = []
    for i in db:
        ls.append({'name':i['name'], 'use':i['use'], 'date':i['date']})
    return ls

@app.post("/info/")
async def create_info(data:Data):
    d = [0]*16
    df = data.dict()
    d[df['num']] = 1
    df['use'] = d
    df['date'] = str(datetime.now())
    db.append(df)
    return db[-1]