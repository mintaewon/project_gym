from datetime import timedelta, datetime
from fastapi import APIRouter, Request, Depends, Form, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.hashing import Hasher
from app.crud import get_user
from jose import JWTError, jwt
from app.config import setting

SECRET_KEY = "d4b784c9e145d5b6da88e7eb57007583dbf7bbeb13b8626af4a27fe0b57462fb"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

templates = Jinja2Templates(directory="./front")

# 첫화면 로그인 페이지
@router.get("/", response_class=HTMLResponse)
def signin_page(request : Request):
    return templates.TemplateResponse("signin.html", {'request':request})

@router.post("/")
async def signin(response:Response, request:Request,form_data:OAuth2PasswordRequestForm=Depends(), useremail:str = Form(), userpassword:str=Form(), db:Session = Depends(get_db)):
    userinfo = get_user(db=db, user_email=useremail)
    errors=[]
    if userinfo:
        if Hasher.verify_password(userpassword, userinfo.password):
            data = {"sub":useremail, "exp":datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}
            access_token = jwt.encode(data, setting.SECRET_KEY, setting.ALGORITHM)
            print('성공')
            response = templates.TemplateResponse("home.html", {'request':request})
            response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
            return response
        else:
            print('실패')
            errors.append("비밀번호를 확인해 주세요")
            return templates.TemplateResponse("signin.html", {'request':request, 'errors':errors})
    else:
        errors.append("아이디를 확인해 주세요")
        return templates.TemplateResponse("signin.html", {'request':request, 'errors':errors})
