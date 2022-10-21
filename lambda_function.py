import sys
import logging
import pymysql
import json
from urllib.parse import unquote

#rds settings

rds_host = "databasenhom14.cs311qcbzfpy.us-east-1.rds.amazonaws.com"
name = "admin"
password = "dangkhoa"
db_name = "ManageUser"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

def lambda_handler(event, context):
    data = event['Records'][0]['body']
    data = unquote(data)
    data = data.replace("\'", "\"")
    print(data)
    data = json.loads(data)
    response = create_mysql(data)

def create_mysql(event):
    try:
        with conn.cursor() as cur:
            str = "create database " + event['name_database']
            cur.execute(str)
        conn.commit()
    except Exception as e: print(e)

