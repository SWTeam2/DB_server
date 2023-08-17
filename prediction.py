import psycopg2
import json
import os

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

json_data = [
    {
        'inference_time': '09:02:10',
        'prediction': 0,
        'timestamp': '08:33:01'
    },
    {
        'inference_time': '10:15:30',
        'prediction': 1,
        'timestamp': '10:00:05'
    },
    {
        'inference_time': '11:45:20',
        'prediction': 2,
        'timestamp': '11:30:45'
    },
    {
        'inference_time': '13:20:15',
        'prediction': 3,
        'timestamp': '13:10:10'
    }
]

cur = conn.cursor()

table_name = 'prediction_table_ex'

create_table_sql = f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        pred_id serial PRIMARY KEY,
        inference_time time,
        prediction float,
        timestamp time
    );
'''
cur.execute(create_table_sql)

insert_sql = f'''
    INSERT INTO {table_name} (inference_time, prediction, timestamp) 
    VALUES (%s, %s, %s)
    RETURNING pred_id;
'''

for data in json_data:
    inference_time = data["inference_time"]
    prediction = data["prediction"]
    timestamp = data["timestamp"]

    cur.execute(insert_sql, (inference_time, prediction, timestamp))
    pred_id = cur.fetchone()[0]
    conn.commit()
    print(f"Data with pred_id {pred_id} has been imported into the table.")

cur.close()
conn.close()
