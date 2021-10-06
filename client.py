from tkinter import *
import time
import TCPCLIENT
import PS4CONTROLLER
import webbrowser
import threading

Ps4Controller = PS4CONTROLLER.PS4()

prozess = threading.Thread(target=Ps4Controller.start,args=())
prozess.start()

programmstart = time.time()

TcpClient = TCPCLIENT.TCP_CLIENT()
TcpClient.setHostPort('xmoo-master.local',65432)
TcpClient.connect()

def callback(url):
    webbrowser.open_new(url)

def tick():
    checkconnection()
    checkPS4Controller()
    fenster.after(1000, tick) 

def checkconnection():
    data = int(time.time() - programmstart + 1)
    data = "ping: " + str(data)
    if TcpClient.send(data.encode()):
        connect_Button.config(bg="green")
        statusbarXmoo.config(bg="green")
    else:
        connect_Button.config(bg="red")
        statusbarXmoo.config(bg="red")

def checkPS4Controller():
    if Ps4Controller.connected:
        statusbarPS4.config(bg="green")
    else:
        statusbarPS4.config(bg="red")

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

# Frames erstellen
Rahmen1 = Frame(master=fenster)

# Buttons erstellen
up_Button = Button(fenster, text = "UP (w)", command=up, height = 2)
right_Button = Button(Rahmen1, text = "RIGHT (d)", command=right, height = 2)
left_Button = Button(Rahmen1, text = "LEFT(a)", command=left, height = 2)
down_Button = Button(fenster, text = "DOWN (s)", command=down, height = 2)
stop_Button = Button(fenster, text= "STOP (q)", command =stop , height = 2)
connect_Button = Button(fenster, text = "Connect", command=TcpClient.connect, height = 2,bg="red")
DatabaseURLLabel = Label(fenster, text= "API URL", cursor="hand2",fg='blue')
statusbarPS4 = Label(fenster, text="PS4 Controller", bd=1, relief=SUNKEN, anchor=W)
statusbarXmoo = Label(fenster, text="xMoo Connection", bd=1, relief=SUNKEN, anchor=W)

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
Rahmen1.pack()
left_Button.pack(side = 'left')
down_Button.pack()
right_Button.pack(side = 'right')
stop_Button.pack(padx=5,pady=20)
DatabaseURLLabel.pack()
DatabaseURLLabel.bind("<Button-1>", lambda e: callback("http://xmoo-master.local:5000/api/telemetrie"))
statusbarPS4.pack(side=BOTTOM, fill=X)
statusbarXmoo.pack(side=BOTTOM, fill=X)

tick()
# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()