from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import signup, signin, collect

import app.models as models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# static 파일 사용
app.mount("/static", StaticFiles(directory="./front/static"), name="static")

app.include_router(signup.router)
app.include_router(signin.router)
app.include_router(collect.router)