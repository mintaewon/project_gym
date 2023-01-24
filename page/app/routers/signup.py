from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from app.schemas import UserCreate, UserBase
from app.crud import create_user, get_user
from app.hashing import Hasher
from sqlalchemy.orm import Session
from app.database import get_db


router = APIRouter()

templates = Jinja2Templates(directory="./front")

# 회원가입 요청
@router.post("/signup",tags=["signup"], response_class=RedirectResponse, status_code=302)
async def signin(username:str = Form(), useremail:str = Form(), userpassword:str = Form(), db:Session = Depends(get_db)):
    userinfo = UserCreate
    userinfo.email = useremail
    userinfo.name = username
    userinfo.password = Hasher.get_hash_password(userpassword)
    create_user(db=db, user=userinfo)
    return "/"

# 회원가입 페이지
@router.get("/signup",tags=["signup"], response_class=HTMLResponse)
def signin_page(request : Request):
    return templates.TemplateResponse("signup.html", {'request':request})

# 아이디 중복확인
@router.post("/emailcheck", tags=["signup"])
async def check_id(useremail:UserBase, db:Session = Depends(get_db)):
    user = get_user(db=db, user_email=useremail.email)
    if user:
        print(1)
        return False
    else:
        print(2)
        return True