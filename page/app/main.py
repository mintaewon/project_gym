from datetime import datetime
from fastapi import FastAPI, Request, Form
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
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
app.mount("/static", StaticFiles(directory="./front/static"), name="static")

# fastapi에서 html 전송하기 위한 jinja2 사용
templates = Jinja2Templates(directory="./front")

# 현재 시간 가져오기
def now_date_time():
    tz = pytz.timezone('Asia/Seoul')
    return datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

# 첫화면 로그인 페이지
@app.get("/", response_class=HTMLResponse)
def login(request : Request):
    return templates.TemplateResponse("login.html", {'request':request})

# 수집 메인 페이지
@app.post("/home", response_class=HTMLResponse)
def home(request : Request):
    return templates.TemplateResponse("home.html", {'request':request})

# 백엔드 동작 확인용
@app.get("/info")
async def get_info():
    ls = []
    for i in db:
        ls.append({'date':i['date'], 'weather':i['weather'], 'use':i['use']})
    return ls

# 클라이언트 데이터 받아오기
@app.post("/info")
async def create_info(data:Data):
    df = data.dict()
    df['date'] = now_date_time()
    db.append(df)
    query_data = []
    query_data.append(df['date'])
    query_data.append(df['weather'])
    query_data.append("d" + ("".join(map(str, df['use']))))  # csv 파일로 받아올때, 0이 사라지는 것 방지
    insert_data(tuple(query_data))
    return db[-1]

# DB 데이터 받아온 후 
@app.get("/down")
async def down_data():
    data = pd.DataFrame(select_data())
    response = StreamingResponse(io.StringIO(data.to_csv(index=False)), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    return response

@app.post("/test")
async def test(form : str):
    print(form)
    return form