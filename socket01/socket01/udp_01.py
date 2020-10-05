#服务端
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',10021))
print('UDP连接')
while True:
    data,addr = s.recvfrom(1024)
    print('收到数据%s:%s.'%addr)
    print(data)
    s.sendto(data.decode('utf-8').upper().encode(),addr)   #数据大写送回客户端