import json
import psycopg2

def connect_db(Database):
    with open("server/.env/id.txt", "r") as f:
        user = f.read()
    with open("server/.env/pw.txt", "r") as f:
        password = f.read()
    conn = psycopg2.connect(
        host="engineer.i4624.tk",  # Server
        database='factory',  # User & Default database
        user=user,  # User & Default database
        password=password,  # Password
        port=50132)  # Port
    # Call the function to create the table if it doesn't exist
    create_table_if_not_exists(conn, Database)
    return conn


def create_table_if_not_exists(conn, name):
    cur = conn.cursor()
    query = f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '{name}')"
    # Check if the table exists
    cur.execute(query)
    table_exists = cur.fetchone()[0]

    if not table_exists:
        print(f"Table {name} does not exists.")
    cur.close()


def contact_pred_id(table, pred_id):
    conn = connect_db(table)
    cur = conn.cursor()
    #SELECT * FROM public.
    query = f"SELECT * FROM public.{table} WHERE pred_id = {pred_id}"

    # SQL 쿼리 실행
    cur.execute(query)

    # 결과 가져오기
    rows = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]

    # 결과를 딕셔너리 형태로 변환
    data_as_dict = [dict(zip(column_names, row)) for row in rows]


    # 커서 및 연결 종료
    cur.close()

    return data_as_dict


# data =  contact_data('learning_table16', '1')
