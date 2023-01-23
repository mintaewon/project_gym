from .config import setting
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{setting.MYSQL_USER}:{setting.MYSQL_PASSWORD}@{setting.MYSQL_HOST}:{setting.MYSQL_PORT}/{setting.MYSQL_DATABASE}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()