from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from app.schemas import User, UserBase
from app.crud import create_user
from app.hashing import Hasher
from sqlalchemy.orm import Session
from app.database import get_db


router = APIRouter()

templates = Jinja2Templates(directory="./front")

# 회원가입 요청
@router.post("/signup",tags=["signup"], response_class=RedirectResponse, status_code=302)
async def signin(username:str = Form(), userid:str = Form(), userpassword:str = Form(), db:Session = Depends(get_db)):
    userinfo = User
    userinfo.id = userid
    userinfo.name = username
    userinfo.password = Hasher.get_hash_password(userpassword)
    create_user(db=db, user=userinfo)
    return "/"

# 회원가입 페이지
@router.get("/signup",tags=["signup"], response_class=HTMLResponse)
def signin_page(request : Request):
    return templates.TemplateResponse("signup.html", {'request':request})

# 아이디 중복확인
@router.post("/idcheck", tags=["signup"])
async def check_id(userid:UserBase):
    print(userid)
    return userid