#!/usr/bin/env python3

import socket
import sys

class TCP_CLIENT():

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def setHostPort(self,Host,Port):
        self.Host = Host
        self.Port = Port

    def connect(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.Host, self.Port))
        except:
            print("Unexpected error tcpclient.py connect(): " + str(sys.exc_info()))

    def send(self, data_send):
        try:
            self.s.sendall(data_send)
            data = self.s.recv(1024)
            if data_send == data:
                return True
            else:
                return False
        except:
            print("Unexpected error tcpclient.py send(): " + str(sys.exc_info()))
            self.connect()
            return False

    def close(self):
        self.s.close()


# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     while True:
#         s.sendall(b'Hello, world')
#         data = s.recv(1024)
#         print('Received', repr(data))
