#!/usr/bin/env python3

import socket
import sys

HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
#while True:
class TCP():

    def __init__(self):
        self.Direction = ""
        self.Ping = 0
        pass
    
    def getDirection(self):
        return self.Direction
    
    def setDirection0(self):
        self.Direction = ""

    def server(self):
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind((HOST, PORT))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    while True:
                        data = conn.recv(1024)
                        #print(data.decode())
                        daten = data.decode().split()
                        print(daten)
                        if daten[0] == "ping:":
                            print("Ping" + daten[1])
                        if daten[0] == "direction:":
                            print("Direction" + daten[1])
                            self.Direction = daten[1]
                        print(self.Direction)
                        
                        #self.Direction = data.decode()
                        if not data:
                            self.Direction = "STOP"
                            print("STOPPPPPPP!!!!!")
                            pass #TODO
                        if data == b'':
                            self.Direction = "STOP"
                            #self.Direction = data.decode()
                            pass #TODO
                        conn.sendall(data)
            except:
                self.Direction = "STOP"
                print("Unexpected error typserver.py server(): " + str(sys.exc_info()))
