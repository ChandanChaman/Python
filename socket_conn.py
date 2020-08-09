"""Make connection to webpage & read data """

import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
url = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(url)

while True:
    data = mysock.recv(1)
    if len(data) <1:
        break
    print (data.decode(),end='')

mysock.close()
