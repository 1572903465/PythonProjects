from flask import Flask, render_template, g, request, url_for, session, redirect
import game.game
import sqlite3
import database.connectData
import user.user
import baiduyun.baiduyuying
from flask_socketio import SocketIO, emit

# app = Flask(__name__, static_url_path="/")
app = Flask(__name__)
app.config['SECRET_KEY']="sdfklas0lk42j"
socketio = SocketIO(app)

game1 = game.game.Game()

@app.route('/')
def test():
    return render_template("login.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        session.pop('user_id',None)
        username = request.form.get("username",None)
        password = request.form.get("password",None)
        # 代理模式
        clint = user.user.Proxy()
        result = clint.IsPassWord(username,password)
        print(result)
        if result:
            g.user = result
            print(g.user)
            return render_template("gobang.html")
    return render_template("login.html")



@app.route("/profile")
def profile():
    if not g:
        return  redirect(url_for('login'))
    return render_template('gobang.html')

@app.route('/down',methods=['GET','POST'])
def down():
    # print("111111111111111")
    # print(request.args)
    # print(request)
    game1 = game.game.Game()
    chessdown = []
    chessdown.append(int(request.args.get("pointX","")))
    chessdown.append(int(request.args.get("pointy", "")))
    chessdown.append(int(request.args.get("color", "")))
    game1.add_piont(chessdown)
    # if chessdown not in game1.points:
    #     game1.points.append(chessdown)
    # chessdown = request.GET.get("name")
    print(game1.points)
    win = game1.CheckWin(chessdown[0],chessdown[1],chessdown[2])
    print(win,"-------------")
    if win and chessdown[2] == 0:
        return {"success": 0}
    elif win and chessdown[2] == 1:
        return {"success": 1}
    return {"success": 3}

# 悔棋
@app.route('/regret',methods=['GET','POST'])
def regret():
    print("111111111111111")
    # print(request.args)
    # print(request)
    game1 = game.game.Game()
    game.game.Game.points.pop()
    #
    # if chessdown not in game.game.Game.points:
    #     game.game.Game.points.append(chessdown)
    # chessdown = request.GET.get("name")
    print(game.game.Game.points)
    return {"success": 0}

# 刷新或者重新开始游戏清除points
@app.route('/clearPoints',methods=['GET','POST'])
def clearPoints():
    print('clearclear')
    game1 = game.game.Game()
    game1.points.clear()
    return {"success": 0}

@socketio.on('luying', namespace='/test_conn')
def get_luying(data):
    with open('D:\\file.wav','wb') as f:
        f.write(data)
    # print(data)
    yuyingshibie = baiduyun.baiduyuying.YuyinShibie()
    count,chess_position = yuyingshibie.analyze_file()
    if count:
        game1 = game.game.Game()
        chess_position.append(len(game1.points)%2)
        flag = game1.add_piont(chess_position)
        if flag:
            emit('chess_position',{'code': '200', 'x': chess_position[0], "y": chess_position[1], "z": chess_position[2]})
            print(game1.points)
            win = game1.CheckWin(chess_position[0], chess_position[1], chess_position[2])
            print(win, "-------------")
            if win and chess_position[2] == 0:
                emit('win',{'code': '200', 'msg':"黑棋胜利"})
            if win and chess_position[2] == 1:
                emit('win',{'code': '200', 'msg':"白棋胜利"})

    print(count,chess_position)


if __name__ == '__main__':
    # 运行本项目，host=0.0.0.0可以让其他电脑也能访问到该网站，port指定访问的端口。默认的host是127.0.0.1，port为5000
    app.run(host='127.0.0.1',port=5000)