from socket import *
import time

HOST = '127.0.0.2'
PORT = 50001
s = socket(AF_INET,SOCK_STREAM)
s.connect((HOST, PORT))
while True:

    s.send(b"Hello World")
    data = s.recv(1024)
    #s.close()
    print("Received",repr(data))   #repr() 转化为字符串
    time.sleep(10)
