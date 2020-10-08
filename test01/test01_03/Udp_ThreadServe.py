from socket import *
import threading
import time


data=None
addr=None

def listen_Message():
    while True:
        global data,addr                                #global全局变量
        data,addr = udp_serve.recvfrom(1024)
        if (data is not None):
          #  print("滴滴：主人，您收到了一条新消息")
            print("您收到的新消息:", data.decode("utf-8"))
            data = None
        #return data,addr
def view_Message():
    global data
    time.sleep(0.5)
    print("您收到的新消息:",data.decode("utf-8"))
    data=None

def send_Message():
    while True:
        global addr
        if(addr is not None):
            time.sleep(0.1)
            data_send = input("请输入你的信息：\n")
            udp_serve.sendto(data_send.encode("utf-8"),addr)

udp_serve = socket(AF_INET,SOCK_DGRAM)
host = "127.0.0.3"
port = 8818
udp_serve.bind((host,port))
print("欢迎来到新新聊天室")
th01 = threading.Thread(target=listen_Message)
th02 = threading.Thread(target=send_Message)
th01.start()
th02.start()





