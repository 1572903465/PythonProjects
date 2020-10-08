import threading
from socket import *
import time

data = None
addr = None
data_arr =[]
def send_Message():
    data_send = input("请输入你的信息:").encode("utf-8")
    upd_client.sendto(data_send, address)

def receive_Message():
    global data,data_arr
    for i in range(len(data_arr)):
        print("您收到的新消息:",data_arr[i])
    data_arr.clear()

def liten_Message():
    while True:
        global data, addr,data_arr  # global全局变量
        data,addr = upd_client.recvfrom(1024)
        if (data is not None):
            print("滴滴：主人，您收到了一条新消息")
            data_arr.append(data.decode("utf-8"))

def fristSend_Message():
    data_send = input("请先跟对方打个招呼吧:").encode("utf-8")
    upd_client.sendto(data_send, address)

if __name__ == '__main__':
    address=("127.0.0.2",8818)
    print("欢迎来到新新聊天室")
    upd_client = socket(AF_INET, SOCK_DGRAM)
    fristSend_Message()
    th02 = threading.Thread(target=liten_Message)
    th02.start()
    while True:
        if(data is not None):
            while True:
                time.sleep(0.5)
                data_choice = input("请选择你的功能 按1接受消息，按2发送消息，按3接受消息并发送消息：\n")
                if(data_choice == "1"):
                    if data_arr:
                        receive_Message()
                    else:
                        print("对方未发送新消息！")
                        continue
                elif(data_choice == "2"):
                    send_Message()
                elif(data_choice == "3"):
                    if data_arr:
                        receive_Message()
                    else:
                        print("对方未发送新消息！")
                    send_Message()
                else:
                    print("输入错误请重新输入")
                    continue






