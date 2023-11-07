# pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
    host='127.0.0.1',
    port='3305',
    user='root',
    password='python',
    database='python'
)

def select_all(): #조회 함수생성
    
    cur = mydb.cursor()                     #커서 객체생성
    sql ="SELECT * FROM emp"     #조회 SQL

    cur.execute(sql)                        #커서를 통한 SQL실행
    result = cur.fetchall()      #커서의 결과를 담는 객체

    for x in result:
        print(x)

select_all()                                #함수 실행