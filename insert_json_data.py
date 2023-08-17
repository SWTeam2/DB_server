import psycopg2
import json
import os

def connect_db():
    with open("server/.env/id.txt", "r") as f:
        user = f.read()

    with open("server/.env/pw.txt", "r") as f:
        password = f.read()

    conn = psycopg2.connect(
        host="engineer.i4624.tk",
        database="factory",
        user=user,
        password=password,
        port=50132,
    )
    return conn

def create_table_if_not_exists(conn, name):
    cur = conn.cursor()
    query = f"CREATE TABLE IF NOT EXISTS {name} (pred_id serial PRIMARY KEY, inference_time varchar, prediction float, timestamp varchar);"
    cur.execute(query)
    conn.commit()
    cur.close()

def insert_json_data(conn, table_name, json_data):
    cur = conn.cursor()

    inference_time = json_data["inference_time"]
    prediction = json_data["prediction"]
    timestamp = json_data["timestamp"]

    insert_sql = f'''
        INSERT INTO {table_name} (inference_time, prediction, timestamp) 
        VALUES (%s, %s, %s)
        RETURNING pred_id;
    '''
    cur.execute(insert_sql, (inference_time, prediction, timestamp))
    pred_id = cur.fetchone()[0]
    conn.commit()

    cur.close()

    return pred_id

def main():
    conn = connect_db()

    table_name = 'prediction_table_ex'
    create_table_if_not_exists(conn, table_name)

    json_data = {
        'inference_time': '09:02:20',
        'prediction': 0.12748925,
        'timestamp': '08:33:11'
    }

    pred_id = insert_json_data(conn, table_name, json_data)
    
    conn.close()

    print(f"Data with pred_id {pred_id} has been imported into the table.")

if __name__ == "__main__":
    main()
