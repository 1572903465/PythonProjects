import json
import pymysql
from flask import Flask, request, render_template

app = Flask(__name__)

# 建立数据库连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    db='Android',
    charset='utf8'
)

@app.route('/')
def hello_world():
    return render_template('login.html',message="哈哈哈哈")



@app.route('/login',methods=['POST'])
def login():
    # 获取post请求的数据
    data_list = []
    # data = json.loads(request.get_data(as_text=True))
    # print(data)
    username = request.form.get('username')
    password = request.form.get('password')

    cursor = conn.cursor()
    sql = 'select * from User where username=%s'
    rows = cursor.execute(sql, args=(username,))
    allUser = cursor.fetchall()
    print(allUser)
    # 判断是否有用户名和密码匹配上
    flag = 0
    for user in allUser:
        if user[1]==password:
            flag = 1
            break
    code = 0
    message = ''
    data = []

    if flag == 1:
        code = 200
        message = '登录成功'
    else:
        code = 400
        message = '用户名或者密码错误'
    return_str = {
        'code': code,
        'message': message,
        'data': data
    }
    return render_template('LoginSuccess.html',code = return_str.get('code'),message = return_str.get('message'))


if __name__ == '__main__':
    app.run(debug=True,port=7000)
