import socket
def send_file_to_client(new_client_socket,client_addr):
    #接受客户端 需要下载的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")

    print("客户端（%s）需要下载文件是：%s" % (str(client_addr), file_name))
    file_content = None
    #2.打开这个文件，读取数据
    try:
        f = open(file_name,"rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件（%s)"%file_name)
    if file_content:
        #3.发送文件的数据给客户端
        new_client_socket.send(file_content)

def main():
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    tcp_server_socket.bind(('127.0.1.2',7890))

    tcp_server_socket.listen(128)
    while True:
        new_client_socket,client_addr = tcp_server_socket.accept()  #返回值 一个套接字连接用来发送和接收数据 ，客户端地址元组

        send_file_to_client(new_client_socket,client_addr)

        new_client_socket.close()

    tcp_server_socket.close()

if __name__ == '__main__':
    main()