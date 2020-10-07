import threading
from socket import *


data = None
addr = None

def send_Message():
    data_send = input("please inout your message:").encode("utf-8")
    upd_client.sendto(data_send, address)

def receive_Message():
    global data, addr  # global全局变量
    data, addr = upd_client.recvfrom(1024)
    if (data is not None):
        print("滴滴：主人，您收到了一条新消息")

def liten_Message():
    global data, addr
    data, addr = upd_client.recvfrom(1024)




address=("127.0.0.2",8818)
print("欢迎来到新新聊天室")
upd_client = socket(AF_INET, SOCK_DGRAM)
while True:
     data=None
    # th02 = threading.Thread(target=liten_Message)
    # th02.start()
    # if(data is not None):
    #     while True:
    #         data_choice = input("请选择你的功能 按1接受消息，按2发送消息，按3接受消息并发送消息：\n")
    #         if(data_choice == "1"):
    #             if (data is not None):
    #                 print("对方未发送新消息！")
    #             else:
    #                 receive_Message()
    #         elif(data_choice == "2"):
    #             send_Message()
    #         elif(data_choice == "3"):
    #             if(data is not None):
    #                 print("对方未发送新消息！")
    #             else:
    #                 receive_Message()
    #             send_Message()
    #         else:
    #             print("输入错误请重新输入")
    #             continue





