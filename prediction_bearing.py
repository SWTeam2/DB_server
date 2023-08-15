import psycopg2
import json
import os
import csv

with open("./.env/id.txt", "r") as f:
    user = f.read()

with open("./.env/pw.txt", "r") as f:
    password = f.read()

conn = psycopg2.connect(
    host="engineer.i4624.tk",
    database="factory",
    user=user,
    password=password,
    port=50132,
)

# JSON 파일 경로
json_file_path = "/path/to/your/json/file.json"

# 데이터베이스 연결
cur = conn.cursor()

# 테이블 생성
table_name = 'Prediction_bearing_table'

# 테이블 생성 구문
create_table_sql = f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        pred_id integer PRIMARY KEY,
        inference_id integer,
        prediction float,
        timestamp timestamp
    );
'''
cur.execute(create_table_sql)

# JSON 파일 읽기 및 데이터 삽입
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)
    for data in json_data:
        inference_id = data["inference_id"]
        prediction = data["prediction"]
        timestamp = data["timestamp"]
        
        insert_sql = f'''
            INSERT INTO {table_name} (inference_id, prediction, timestamp) 
            VALUES (%s, %s, %s);
        '''
        cur.execute(insert_sql, (inference_id, prediction, timestamp))
conn.commit()

# 연결 종료
cur.close()
conn.close()

print("JSON data from file has been imported into the table.")
