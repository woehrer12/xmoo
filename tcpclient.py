#!/usr/bin/env python3

import socket
import sys

HOST = 'xmoo-master.local'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect():
    try:
        s.connect((HOST, PORT))
    except:
        print("Unexpected error typclient.py connect(): " + str(sys.exc_info()))

def send(data_send):
    try:
        s.sendall(data_send)
        data = s.recv(1024)
        if data_send == data:
            return True
        else:
            return False
    except:
        print("Unexpected error typclient.py send(): " + str(sys.exc_info()))
        return False

def close():
    s.close()


# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     while True:
#         s.sendall(b'Hello, world')
#         data = s.recv(1024)
#         print('Received', repr(data))
