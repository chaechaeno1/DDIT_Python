import pymysql
from sqlalchemy.dialects.mysql.pymysql import MySQLDialect_pymysql
 
# MySQL에 연결
conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', port=3305, charset='utf8')

e_id = "5"
e_name = "5"
gen = "5"
addr = "5"

curs = conn.cursor()

# 수정된 SQL 쿼리에는 각 변수 주변에 따옴표(')를 추가했습니다.
sql = f"""insert into emp
        (e_id, e_name, gen, addr)
        values
        ('{e_id}', '{e_name}', '{gen}', '{addr}')
"""




cnt = curs.execute(sql)
print(curs.rowcount)
print(cnt)

conn.commit()

curs.close()
conn.close()             