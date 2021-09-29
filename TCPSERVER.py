#!/usr/bin/env python3

import socket
import sys

class TCP():

    def __init__(self):
        self.Direction = ""
        self.Ping = 0
        self.IP = False
    
    def setHostPort(self,Host,Port):
        self.Host = Host
        self.Port = Port

    def getDirection(self):
        return self.Direction
    
    def setDirection0(self):
        self.Direction = ""
        self.Ping = ""

    def server(self):
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind((self.Host, self.Port))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    self.IP = addr[0]
                    #print('Connected by', addr)
                    while True:
                        data = conn.recv(1024)
                        #print(data.decode())
                        daten = data.decode().split()
                        #print(daten)
                        if daten[0] == "ping:":
                            #print("Ping" + daten[1])
                            self.Ping = daten[1]

                        if daten[0] == "direction:":
                            #print("Direction" + daten[1])
                            self.Direction = daten[1]
                        #print(self.Direction)
                        
                        #self.Direction = data.decode()
                        if not data:
                            self.Direction = "STOP"
                            #print("STOPPPPPPP!!!!!")
                            pass #TODO
                        if data == b'':
                            self.Direction = "STOP"
                            #self.Direction = data.decode()
                            pass #TODO
                        conn.sendall(data)
            except:
                s.close()
                self.IP = False
                self.Direction = "STOP"
                print("Unexpected error typserver.py server(): " + str(sys.exc_info()))
