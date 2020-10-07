from socket import *

udp = socket(AF_INET,SOCK_DGRAM)
while True:
    data = input("input your message:")
    udp.sendto(data.encode("utf-8"),("127.0.0.1",8888))
    print(udp.recv(1024).decode("utf-8"))
udp.close()