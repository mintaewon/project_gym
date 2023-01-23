import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../page/.env')

class Settings:
    MYSQL_USER=os.getenv("MYSQL_USER")
    MYSQL_PASSWORD=os.getenv("MYSQL_PASSWORD")
    MYSQL_HOST=os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT=os.getenv("MYSQL_PORT", 3306)
    MYSQL_DATABASE=os.getenv("MYSQL_DATABASE", "test")

setting = Settings()