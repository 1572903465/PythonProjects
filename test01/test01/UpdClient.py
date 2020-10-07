from socket import *
def sendMessage():
    data_send = input("please inout your message:").encode("utf-8")
    upd_client.sendto(data_send, address)
def chatRoom():
    if (data == b''):
        print("对方并不是太想搭理你，并向你扔了一个西红柿")
    while True:
        data_choice = input("请选择你的功能：按1接受消息；按2发送消息；按3接受并发送消息；按0不接收消息并退出")
        if (data == '1'):
            print('messages received:', data.decode("utf-8"))
        elif (data_choice == '2'):
            if (data is None):
                print("你没有收到字符串不能发送消息")
            send_data = input("input your message:")
            upd_client.sendto(send_data.encode("utf-8"), addr)
        elif (data_choice =='3'):
            print('messages received:', data.decode("utf-8"))
            send_data = input("input your message:")
            upd_client.sendto(send_data.encode("utf-8"), addr)
        elif(data_choice == '0'):
            send_data = ""
            upd_client.sendto(send_data.encode("utf-8"), addr)
            print("你已成功退出")
            break
        else:
            print("输入错误请重新输入")

address=("127.0.0.2",8818)
print("欢迎来到新新聊天室")
while True:
    upd_client = socket(AF_INET, SOCK_DGRAM)
    sendMessage()
    data, addr = upd_client.recvfrom(1024)
    if (data == b''):
        print("对方并不是太想搭理你，并向你扔了一个西红柿")
    else:
        chatRoom()

