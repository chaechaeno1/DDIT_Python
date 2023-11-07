import pymysql
from sqlalchemy.dialects.mysql.pymysql import MySQLDialect_pymysql
 
# MySQL에 연결
conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', port=3305, charset='utf8')

e_id = "5"

curs = conn.cursor()

# 수정된 SQL 쿼리에는 각 변수 주변에 따옴표(')를 추가했습니다.
sql = f"""
    delete from emp
    where e_id='{e_id}'   
"""


cnt = curs.execute(sql)
print(cnt)
#print(curs.rowcount)


conn.commit()

curs.close()
conn.close()             