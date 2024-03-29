import pymysql
class DaoMem:
    
    def __init__(self): #생성자
        self.conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', port=3305, charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):
        sql = "select * from member"
        self.curs.execute(sql)
         
        list = self.curs.fetchall()
        return list  
    
    def selectOne(self, m_id):
        sql = f"""
            select * from member 
            where 
                e_id='{m_id}'
        """
        self.curs.execute(sql)
        
        # vos = self.curs.fetchall()
        vo = self.curs.fetchone()
        return vo
    
    def insert(self,m_id,m_name,tel,email):
        sql = f"""
            insert into member
            (m_id, m_name, tel, email)
            values
            ('{m_id}', '{m_name}', '{tel}', '{email}')
        """
        
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self,m_name,tel,email,m_id):
        sql = f"""
            update member
            set
                m_name='{m_name}',
                tel='{tel}',
                email='{email}'
            where 
                m_id='{m_id}'    
        """        
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self,m_id):
        sql = f"""
            delete from member
            where m_id='{m_id}'   
        """      
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt    
    
    

    def __del__(self):
        self.curs.close()
        self.conn.close()   
        
        
if __name__ == '__main__':
        de = DaoMem()
        cnt = de.insert('1','1','1','1')
        print(cnt)
    