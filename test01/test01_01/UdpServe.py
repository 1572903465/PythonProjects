from socket import *
import threading
import time
data=None
addr=None
data_arr = []

def listen_Message():
    while True:
        global data,addr                               #global全局变量
        data,addr = udp_serve.recvfrom(1024)
        if (data is not None):
            print("滴滴：主人，您收到了一条新消息")
            data_arr.append(data.decode("utf-8"))
def view_Message():
    global data
    for i in range(len(data_arr)):
        print("您收到的新消息:", data_arr[i])
    data_arr.clear()
    data=None

def send_Message():
    data_send = input("请输入你的信息：")
    udp_serve.sendto(data_send.encode("utf-8"),addr)

if __name__ == '__main__':
    udp_serve = socket(AF_INET,SOCK_DGRAM)
    host = "127.0.0.2"
    port = 10002
    udp_serve.bind((host,port))
    print("欢迎来到新新聊天室")
    th01 = threading.Thread(target=listen_Message)  #用线程解决了  recvfrom监听等待  和   input等待输入等待冲突的问题
    th01.start()
    while True:
        if(data is not None):
            while True:
                time.sleep(0.5)
                data_choice = input("请选择你的功能 按1接受消息，按2发送消息，按3接受消息并发送消息：\n")
                if(data_choice=="1"):
                    if data_arr:
                        view_Message()
                    else:
                        print("对方还未发送新消息！")
                        continue
                elif(data_choice=="2"):
                    send_Message()
                elif(data_choice=="3"):
                    if data_arr:
                        view_Message()
                    else:
                        print("对方还未发送新消息！")
                    send_Message()
                else:
                    print("输入错误请重新输入")
                    continue




