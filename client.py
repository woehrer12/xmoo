from tkinter import *
import time
from time import gmtime, strftime
import configparser
import os
import tcpclient

programmstart = time.time()

def tick():
    global localzeit
    localzeit = time.strftime('%H:%M:%S')
    localuhr.config(text = localzeit)
    checkconnection()
    localuhr.after(200, tick) 

def checkconnection():
    data = int(time.time() - programmstart + 1)
    try:
        tcpclient.send(data.to_bytes(4, "big"))
    except:
        pass
        #TODO Error Message BOX

def up():
    pass

def down():
    pass

def right():
    pass

def left():
    pass


# Ein Fenster erstellen
fenster = Tk()
# Den Fenstertitle erstellen
fenster.title("xMoo Steuerung")

local_label = Label(fenster, 
                text = "Lokal",
                font=('Arial',30),
                fg='black',
                width = 10,
                height = 1)

localuhr = Label(master=fenster,
            font=('Arial',30),
            fg='black',
            width = 10,
            height = 1)

# Buttons erstellen
#TODO Pfeiltasten
up_Button = Button(fenster, text = "UP", command=up, height = 2)
right_Button = Button(fenster, text = "RIGHT", command=right, height = 2)
left_Button = Button(fenster, text = "LEFT", command=left, height = 2)
down_Button = Button(fenster, text = "DOWN", command=down, height = 2)
try:
    connect_Button = Button(fenster, text = "Connect", command=tcpclient.connect, height = 2)
except:
    pass
    #TODO Error Message Box

#Aufrufe
local_label.pack()
localuhr.pack()
connect_Button.pack()
up_Button.pack()
left_Button.pack(padx=5, pady=10, side=LEFT)
down_Button.pack(padx=5, pady=10, side=LEFT)
right_Button.pack(padx=5, pady=10, side=LEFT)




tick()
# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()