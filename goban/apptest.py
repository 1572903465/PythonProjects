from flask import Flask, render_template, g, request, url_for, session, redirect
import sqlite3
import user


app = Flask(__name__, static_url_path="/")


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        # 创键连接对象
        con = sqlite3.connect('database/userInfo.db')
        # 创键游标对象
        cur = con.cursor()
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        username = 'Admin'
        sql = "select count(*) from user where username = '{0}'".format(username)
        cur.execute(sql)
        Isexites = cur.fetchall()
        if Isexites:
            return redirect(url_for('profile'))

    return render_template("login.html")


if __name__ == '__main__':
    app.run()
