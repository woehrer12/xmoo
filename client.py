from tkinter import *
import time
from time import gmtime, strftime
import configparser
import os
import tcpclient
import sys

programmstart = time.time()

tcpclient.connect()


def tick():
    checkconnection()
    fenster.after(1000, tick) 

def checkconnection():
    data = int(time.time() - programmstart + 1)
    data = "ping: " + str(data)
    if tcpclient.send(data.encode()):
        connect_Button.config(bg="green")
    else:
        connect_Button.config(bg="red")


def up(*args):
    print("UP")
    data = "direction: UP"
    tcpclient.send(data.encode())

def down(*args):
    print("DOWN")
    data = "direction: DOWN"
    tcpclient.send(data.encode())
    pass

def right(*args):
    print("RIGHT")
    data = "direction: RIGHT"
    tcpclient.send(data.encode())
    pass

def left(*args):
    print("LEFT")
    data = "direction: LEFT"
    tcpclient.send(data.encode())
    pass


# Ein Fenster erstellen
fenster = Tk()
# Den Fenstertitle erstellen
fenster.title("xMoo Steuerung")

# Buttons erstellen
up_Button = Button(fenster, text = "UP", command=up, height = 2)
right_Button = Button(fenster, text = "RIGHT", command=right, height = 2)
left_Button = Button(fenster, text = "LEFT", command=left, height = 2)
down_Button = Button(fenster, text = "DOWN", command=down, height = 2)
connect_Button = Button(fenster, text = "Connect", command=tcpclient.connect, height = 2,bg="red")

#Key Bindings
fenster.bind('<Up>',up)
fenster.bind('w',up)
fenster.bind('<Left>',left)
fenster.bind('a',left)
fenster.bind('<Down>',down)
fenster.bind('s',down)
fenster.bind('<Right>',right)
fenster.bind('d',right)





#Aufrufe
connect_Button.pack()
up_Button.pack()
left_Button.pack(padx=5, pady=10, side=LEFT)
down_Button.pack(padx=5, pady=10, side=LEFT)
right_Button.pack(padx=5, pady=10, side=LEFT)




tick()
# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()