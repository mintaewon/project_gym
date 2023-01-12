from typing import Tuple
import pymysql
import json

with open('app/config.json', 'r') as f:
    config = json.load(f)

conn = pymysql.connect(
    host=config['MysqlDB']['HOST'],
    user=config['MysqlDB']['USERNAME'],
    password=config['MysqlDB']['PASSWORD'],
    db=config['MysqlDB']['DATABASE'],
    port=config['MysqlDB']['PORT'],
    charset='utf8',
    )
curs = conn.cursor(pymysql.cursors.DictCursor)

# ==== insert ====
sql = f"INSERT INTO {config['MysqlDB']['TABLENAME']} values (%s, %s, %s)"
selectsql = f"SELECT * FROM {config['MysqlDB']['TABLENAME']}"
def insert_data(df_row:tuple):
    curs.execute(sql, df_row)
    conn.commit()

def select_data():
    curs.execute(selectsql)
    conn.commit()
    return curs.fetchall()