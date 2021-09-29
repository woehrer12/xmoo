from tkinter import *
import time
from time import gmtime, strftime
import configparser
import os
#import tcpclient
import TCPCLIENT
import sys
import TCPSERVER
import threading

programmstart = time.time()

TcpClient = TCPCLIENT.TCP_CLIENT()
TcpClient.setHostPort('xmoo-master.local',65432)
TcpClient.connect()

TcpServer = TCPSERVER.TCP()
TcpServer.setHostPort('0.0.0.0',65431)
prozess = threading.Thread(target=TcpServer.server,args=())
prozess.start()

def tick():
    checkconnection()
    fenster.after(1000, tick) 

def checkconnection():
    data = int(time.time() - programmstart + 1)
    data = "ping: " + str(data)
    if TcpClient.send(data.encode()):
        connect_Button.config(bg="green")
    else:
        connect_Button.config(bg="red")


def up(*args):
    data = "direction: UP"
    TcpClient.send(data.encode())

def down(*args):
    data = "direction: DOWN"
    TcpClient.send(data.encode())

def right(*args):
    data = "direction: RIGHT"
    TcpClient.send(data.encode())

def left(*args):
    data = "direction: LEFT"
    TcpClient.send(data.encode())

def stop(*args):
    data = "direction: STOP"
    TcpClient.send(data.encode())

# Ein Fenster erstellen
fenster = Tk()
# Den Fenstertitle erstellen
fenster.title("xMoo Steuerung")

# Buttons erstellen
up_Button = Button(fenster, text = "UP (w)", command=up, height = 2)
right_Button = Button(fenster, text = "RIGHT (d)", command=right, height = 2)
left_Button = Button(fenster, text = "LEFT(a)", command=left, height = 2)
down_Button = Button(fenster, text = "DOWN (s)", command=down, height = 2)
stop_Button = Button(fenster, text= "STOP (q)", command =stop , height = 2)
connect_Button = Button(fenster, text = "Connect", command=TcpClient.connect, height = 2,bg="red")

#Key Bindings
fenster.bind('<Up>',up)
fenster.bind('w',up)
fenster.bind('<Left>',left)
fenster.bind('a',left)
fenster.bind('<Down>',down)
fenster.bind('s',down)
fenster.bind('<Right>',right)
fenster.bind('d',right)
fenster.bind('q',stop)





#Aufrufe
connect_Button.pack()
up_Button.pack()
left_Button.pack(padx=5, pady=10, side=LEFT)
down_Button.pack(padx=5, pady=10, side=LEFT)
right_Button.pack(padx=5, pady=10, side=LEFT)
stop_Button.pack(padx=5,pady=20)




tick()
# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()