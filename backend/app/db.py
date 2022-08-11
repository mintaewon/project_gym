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
    charset='utf8',
    )
curs = conn.cursor(pymysql.cursors.DictCursor)

# ==== insert ====
sql = """insert into TIMELINE(datetime, weather, Freeweight, SmithMachine, PowerLegPress, PowerRack, InclineBench, FlatBench, ShoulderPressMachine, Cable, LatPulldown, ChestFlyMachine, ChestPressMachine, SeatedRowMachine, LegPressMachine, InnerThighMachine, LegExtension, LegCurl)
         values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

def insert_data(df_row:tuple):
    curs.execute(sql, df_row)
    conn.commit()