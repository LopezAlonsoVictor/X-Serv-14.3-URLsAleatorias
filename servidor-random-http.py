#!/usr/bin/python3

#Víctor López Alonso

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))
mySocket.listen(3)

try:
    while True:
        aux = random.randint(1,999999999)
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('HTTP request received:')
        print(recvSocket.recv(1024))
        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        b"<html><body><h1>Hola. </h1>></body></html>" +
                        b"<a href ='http://localhost:1234/" +
                        bytes(str(aux),'utf-8') +
                        b"'>Dame otra</a>" +
                        b"\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()


