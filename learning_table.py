import psycopg2
import os
import csv

with open(".env/id.txt", "r") as f:
    user = f.read()

    
with open(".env/pw.txt", "r") as f:
    password = f.read()


conn = psycopg2.connect(
    host="engineer.i4624.tk", # Server
    database="factory", # User & Default database
    user=user, # User & Default database
    password=password,  # Password
    port=50132 )# Port

# CSV 파일 디렉토리 설정
csv_directory = '/home/dbuser-4624/dataBase/ieee-phm-2012-data-challenge-dataset-master/Learning_set/Bearing1_1'

# 열 이름 설정
column_names = ['hour', 'minutes', 'second', 'microsecond', 'horiz_accel', 'vert_accel','csv_number']

# 데이터베이스 연결
cur = conn.cursor()

# 테이블 생성
table_name = 'Learning_table3'

# 테이블 생성 구문
create_table_sql = f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id SERIAL PRIMARY KEY,
        hour integer,
        minutes integer,
        second integer,
        microsecond integer,
        horiz_accel float,
        vert_accel float,
        csv_number integer
    );
'''
cur.execute(create_table_sql)

# 커밋
conn.commit()

# CSV 파일 읽기 및 데이터 삽입
csv_files = [f for f in os.listdir(csv_directory) if f.endswith('.csv')]
for csv_file in csv_files:
    csv_file_path = os.path.join(csv_directory, csv_file)
    
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # 첫 번째 행은 건너뛰기 (컬럼 이름)
        for row in reader:
            insert_sql = f'''
                INSERT INTO {table_name} ({', '.join(column_names)}) 
                VALUES ({', '.join(["%s"] * len(column_names))});
            '''
            cur.execute(insert_sql, row)
            conn.commit()

# 연결 종료
cur.close()
conn.close()

print("CSV files have been imported into the table.")
