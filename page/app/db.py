from typing import Tuple
import pymysql
import json

# DB 정보 받아오기
with open('app/config.json', 'r') as f:
    config = json.load(f)

# DB 연결
conn = pymysql.connect(
    host=config['MysqlDB']['HOST'],
    user=config['MysqlDB']['USERNAME'],
    password=config['MysqlDB']['PASSWORD'],
    db=config['MysqlDB']['DATABASE'],
    port=config['MysqlDB']['PORT'],
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
    )



# DB에 적재
def insert_data(df_row:tuple):
    with conn:
        with conn.cursor() as cursor:

            sql = f"INSERT INTO {config['MysqlDB']['TABLENAME']} values (%s, %s, %s)"
            cursor.execute(sql, df_row)
        conn.commit()


# 전체 데이터 가져오기
def select_data():
    with conn:
        with conn.cursor() as cursor:
            selectsql = f"SELECT * FROM {config['MysqlDB']['TABLENAME']}"
            cursor.execute(selectsql)
            total_data = cursor.fetchall()
        return total_data