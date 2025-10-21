# DBMS_mysql.py

import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    # host= "localhost",
    user="root",
    passwd='',
    database="exampledb",
    charset="utf8mb4"
)

# 커서 생성 => 명령어 작성
cursor = conn.cursor()

# 명령어 실행
cursor.execute("SELECT DATABASE()")
print("현재 데이터배이스:",cursor.fetchall())

# 연결 해제
conn.close()