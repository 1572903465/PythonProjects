from flask import Flask, render_template, g, request, url_for, session, redirect
from dataclasses import dataclass

app = Flask(__name__, static_url_path="/")
app.config['SECRET_KEY']="sdfklas0lk42j"

@dataclass
class User:
    id: int
    username:str
    password:str

users = [
    User(1,"Admin","123456"),
    User(2,"Eason","888888"),
    User(3,"Tommy","666666")
]

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [u for u in users if u.id == session['user_id']]
        g.user=user[0]
        print(g)


# @app.route('/')
# def begin():
#     return render_template("login.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':

        session.pop('user_id',None)
        username = request.form.get("username",None)
        password = request.form.get("password",None)
        user = [u for u in users if u.username==username]
        if len(user) > 0:
            user = user[0]
        if user and user.password == password:
            session['user_id'] = user.id
            # print(url_for('profile'))
            # return redirect(url_for('profile'),)
            user = {
                'username':username,
                'uid':user.id
            }
            return render_template("profile.html",userinfo=user)

    return render_template("login.html")

@app.route("/profile")
def profile():
    if not g.user:
        return  redirect(url_for('login'))
    return render_template('profile.html')

if __name__ == '__main__':
    # 运行本项目，host=0.0.0.0可以让其他电脑也能访问到该网站，port指定访问的端口。默认的host是127.0.0.1，port为5000
    app.run(host='127.0.0.1',port=9000)