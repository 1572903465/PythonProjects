from socket import *
import threading
def chat(data,addr):
    if (data == b''):
        print("对方也不是太想搭理你，也向你扔了一个西红柿")
    while True:
        data_choice = input("请选择你的功能：按1接受消息；按2发送消息；按3接受并发送消息；按0不接收消息并退出")
        if (data_choice == '1'):
            print('messages received:', data.decode("utf-8"))
        elif (data_choice == '2'):
            if (data is None):
                print("你没有收到字符串不能发送消息")
            send_data = input("input your message:")
            udp_serve.sendto(send_data.encode("utf-8"), addr)
        elif (data_choice =='3'):
            print('messages received:', data.decode("utf-8"))
            send_data = input("input your message:")
            udp_serve.sendto(send_data.encode("utf-8"), addr)
        elif(data_choice == '0'):
            send_data = ""
            udp_serve.sendto(send_data.encode("utf-8"), addr)
            print("你已成功退出")
            break
        else:
            print("输入错误请重新输入")
        #data, addr = udp_serve.recvfrom(1024)  # 接收1024字节
udp_serve = socket(AF_INET,SOCK_DGRAM)
host = "127.0.0.2"
port = 8818
udp_serve.bind((host,port))
print("欢迎来到新新聊天室")
while True:
    data=None
    data,addr = udp_serve.recvfrom(1024)  # 接收1024字节
    if (data is not None):
        print("你收到了一条消息")
        th01 = threading.Thread(target=chat())
        th02 = threading.Thread(target=chat,args=(data,addr))
        th02.start()


