#!/usr/bin/env python3

import socket
import sys

HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
#while True:
def server():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            #while True:
            data = conn.recv(1024)
            print(data.decode())
            if not data:
                pass #TODO
            if data == b'':
                pass #TODO
            conn.sendall(data)
    except:
        print("Unexpected error typserver.py server(): " + str(sys.exc_info()))
