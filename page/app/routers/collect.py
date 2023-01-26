from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
import pytz
import io
import pandas as pd
from app.schemas import Data
from app.crud import create_item, get_item
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

# fastapi에서 html 전송하기 위한 jinja2 사용
# templates = Jinja2Templates(directory="./front")

# 현재 시간 가져오기
def now_date_time():
    tz = pytz.timezone('Asia/Seoul')
    return datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

# # 수집 메인 페이지
# @router.get("/home", response_class=HTMLResponse)
# def home(request : Request):
#     return templates.TemplateResponse("home.html", {'request':request})

# 클라이언트 데이터 받아오기
@router.post("/info")
async def create_info(data:Data, db:Session = Depends(get_db)):
    iteminfo = Data
    iteminfo.weather = data.weather
    iteminfo.datetime = data.datetime
    iteminfo.use = ("d"+("".join(map(str, data.use))))
    create_item(db=db, data=iteminfo)
    return data.datetime

# DB 데이터 받아온 후 다운로드
@router.get("/down")
async def down_data(db:Session = Depends(get_db)):
    df = get_item(db=db)
    data = pd.read_sql(df.statement, df.session.bind)
    response = StreamingResponse(io.StringIO(data.to_csv(index=False)), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    return response