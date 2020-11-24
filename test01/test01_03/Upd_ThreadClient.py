import threading
from socket import *
import time

data = None
addr = None

def send_Message():
    while True:
        global addr
        if(addr is not None):
            time.sleep(0.1)
            data_send = input("请输入您的信息:\n").encode("utf-8")
            upd_client.sendto(data_send, address)

def receive_Message():
    while True:
        global data
        if (data is not None):
            print("您收到的新消息:",data.decode("utf-8"))
            data=None

def liten_Message():
    while True:
        global data, addr  # global全局变量
        data,addr = upd_client.recvfrom(1024)
        if (data is not None):
#           print("滴滴：主人，您收到了一条新消息")
            print("您收到的新消息:", data.decode("utf-8"))


def fristSend_Message():
    data_send = input("请先跟对方打个招呼吧:").encode("utf-8")
    upd_client.sendto(data_send, address)

address=("127.0.0.3",8818)
print("欢迎来到新新聊天室")
upd_client = socket(AF_INET, SOCK_DGRAM)
fristSend_Message()
th01 = threading.Thread(target=liten_Message)
th02 = threading.Thread(target=send_Message)
th01.start()
th02.start()






