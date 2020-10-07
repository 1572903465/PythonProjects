from socket import *
from time import *

udp_serer = socket(AF_INET,SOCK_DGRAM)
udp_serer.bind(("127.0.0.1",8888))
while True:
    data,addr = udp_serer.recvfrom(1024)
    print("Message:",data.decode("utf-8"),"From Address",addr)
    senddata = (data.decode("utf-8")+str(time())).encode("utf-8")
    udp_serer.sendto(senddata,addr)