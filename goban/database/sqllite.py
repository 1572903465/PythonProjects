import sqlite3

#创键连接对象
con = sqlite3.connect('userInfo.db')

#创键游标对象
cur= con.cursor()

#执行SQL
cur.execute('CREATE TABLE `user` (id int(10) PRIMARY KEY,username varchar(20),password varchar(20))')
data = [(1,"Admin","123456"),(2,"Eason","888888"),(3,"Tommy","666666")]
cur.executemany('insert into user(id,username,password) values (?,?,?)',data)
username = 'Admin'
# sql = "select * from user where username = '{0}'".format(username)
# sql = "select * from user where username = '?'"


# cur.executemany(sql, username)

# cur.execute(sql)

# print(cur.fetchall())

#提交事务
con.commit()

cur.close()
con.close()