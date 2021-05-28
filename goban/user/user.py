import database.connectData


# 异常类用户不存在则抛出异常
class NotFindError(Exception):
    def __init__(self, msg):
        self.msg = msg


# 获取用户是否存在  用户是否密码正确
class UserInfo:
    def __init__(self):
        # 建立数据库工厂实例
        dataFactory = database.connectData.DataFactory()
        name = "sqllite"
        dababase = dataFactory.choice(name)
        # 创键连接对象
        # con = sqlite3.connect('database/userInfo.db')
        # 创键游标对象
        self.cur = dababase.connect()

    def IsUserName(self,username):

        sql = "select count(*) from user where username = ?"
        self.cur.execute(sql,(username,))
        count = self.cur.fetchall()
        print(type(count))

        if count[0][0] == 0:
            return False
        else:
            return True

    def IsPassWord(self,username,password):
        sql = "select * from user where username = ? and password = ?"
        self.cur.execute(sql, (username,password))
        count = self.cur.fetchall()
        print(count)
        if count:
            return True
        else:
            return False

#代理模式
class Proxy:
    def __init__(self):
        self.userInfo = UserInfo()

    def IsUserName(self, username):
        Is = self.userInfo.IsUserName(username)
        if Is:
            print("该用户不存在")
            return False
        else:
            return True

    def IsPassWord(self, username, password):
        Is = self.userInfo.IsPassWord(username,password)
        if Is:
            return True
        else:
            print("用户：%s的密码错误"%username)
            return False


if __name__ == '__main__':
    user = Proxy()
    print(user.IsUserName('Admin'))
    print(user.IsUserName('Admi'))
    user.IsPassWord("Admin","123456")
    user.IsPassWord("Admn", "123456")
