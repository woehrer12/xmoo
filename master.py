import TCPSERVER
import sys
import BTS7960HBridgePCA9685 as HBridge
import os
import threading
import time

# Variablen Definition der linken und rechten Geschwindigkeit der
# Motoren des Roboter-Autos.
speedleft = 0
speedright = 0

def printscreen():
    os.system('clear')
    print("========== Geschwindigkeitsanzeige ==========")
    print("Geschwindigkeit linker Motor:  ", speedleft)
    print("Geschwindigkeit rechter Motor: ", speedright)
    print(TcpServer.getDirection())

#Abarbeitungsschleife

TcpServer = TCPSERVER.TCP()
TcpServer.setHostPort('0.0.0.0',65432)
prozess = threading.Thread(target=TcpServer.server,args=())
prozess.start()

while True:
    #printscreen()
    if(TcpServer.getDirection() == "UP"):
        speedleft = speedleft + 0.1
        speedright = speedright + 0.1
        if speedleft > 1:
            speedleft = 1
        if speedright > 1:
            speedright = 1
        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        TcpServer.setDirection0()

    if(TcpServer.getDirection() == "DOWN"):
        speedleft = speedleft - 0.1
        speedright = speedright - 0.1
        if speedleft < -1:
            speedleft = -1
        if speedright < -1:
            speedright = -1   
        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        TcpServer.setDirection0()

    if(TcpServer.getDirection() == "STOP"):
        speedleft = 0
        speedright = 0
        HBridge.setMotorLeft(0)
        HBridge.setMotorRight(0)

    if(TcpServer.getDirection() == "RIGHT"):      
        speedright = speedright - 0.1
        speedleft = speedleft + 0.1
        if speedright < -1:
            speedright = -1
        if speedleft > 1:
            speedleft = 1
        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        TcpServer.setDirection0()
        
    if(TcpServer.getDirection() == "LEFT"):
        speedleft = speedleft - 0.1
        speedright = speedright + 0.1
        if speedleft < -1:
            speedleft = -1
        if speedright > 1:
            speedright = 1
        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        TcpServer.setDirection0()
