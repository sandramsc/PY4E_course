import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

size = 0
while True:
    data = mysock.recv(3000)
    if len(data) < 1: break
    size = size + len(data)
    print(data.decode(),size, 'total number of characters')
mysock.close()
