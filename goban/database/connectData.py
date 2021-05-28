import sqlite3
import pymysql

# 数据库工厂模式
class SqlLite:
    def connect(self):
        con = sqlite3.connect('userInfo.db')
        cur = con.cursor()
        return cur

    def colse(self):
        cur.close()

class MySql:

    def connect(self):
        # 建立数据库连接
        con = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='userInfo',
            charset='utf8'
        )
        cur = con.cursor()
        return cur

    def colse(self):
        cur.close()

class DataFactory:

    def choice(self,name):
        if name == "sqllite":
            return SqlLite()

        if name == "mysql":
            return MySql()
if __name__ == '__main__':
    data = DataFactory()
    sql = data.choice('sqllite')
    cur = sql.connect()
    sql = "select * from user"
    cur.execute(sql)
    print(cur.fetchall())