from socket import *

HOST = '127.0.0.2'
PORT = 50001
s = socket(AF_INET,SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(2)  #2 最大接受两个的连接
while True:
    conn,addr = s.accept()
    print('Connected by',addr)
    data = conn.recv(1024)
    if not data:break
    conn.send(data)
#conn.close()