from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.connect(('www.baibu.com',80))
s.send(b'GET/HTTP/1.1\r\nHost:www.baidu.com\r\nConnection:close\r\n\r\n')

buf = []
while True:
    d = s.recv(1024)
    if d:
        buf.append(d)
       # print("d:",d)
    else:
        break
data = b"".join(buf)
s.close()
header,html=data.split((b'\r\n\r\n'),1)
print(header.decode('utf-8'))
print(html.decode('utf-8'))