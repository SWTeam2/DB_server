import json
import psycopg2

def connect_db(Database):
    with open(".env/id.txt", "r") as f:
        user = f.read()
    with open(".env/pw.txt", "r") as f:
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
