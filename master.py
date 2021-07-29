import TCPSERVER
import sys
import BTS7960HBridgePCA9685 as HBridge
import os
import readchar
import threading
import time

# Variablen Definition der linken und rechten Geschwindigkeit der
# Motoren des Roboter-Autos.
speedleft = 0
speedright = 0

# Die Funktion getch() nimmt die Tastatureingabe des Anwenders
# entgegen. Die gedrueckten Buchstaben werden eingelesen. Sie werden
# benoetigt um die Richtung und Geschwindigkeit des Roboter-Autos
# festlegen zu koennen.
def getch():
   ch = readchar.readchar()
   return ch

# Die Funktion printscreen() gibt immer das aktuelle Menue aus
# sowie die Geschwindigkeit der linken und rechten Motoren wenn
# es aufgerufen wird.
def printscreen():
    # der Befehl os.system('clear') leert den Bildschirmihalt vor
    # jeder Aktualisierung der Anzeige. So bleibt das Menue stehen
    # und die Bildschirmanzeige im Terminal Fenster steht still.
    os.system('clear')
    print("w/s: beschleunigen")
    print("a/d: lenken")
    print("q:   stoppt die Motoren")
    print("x:   Programm beenden")
    print("========== Geschwindigkeitsanzeige ==========")
    print("Geschwindigkeit linker Motor:  ", speedleft)
    print("Geschwindigkeit rechter Motor: ", speedright)
    print(TcpServer.getDirection())

#Abarbeitungsschleife

TcpServer = TCPSERVER.TCP()
prozess = threading.Thread(target=TcpServer.server,args=())
prozess.start()

while True:
    time.sleep(1)
    printscreen()

    # Mit dem Aufruf der Funktion getch() wird die Tastatureingabe 
    # des Anwenders eingelesen. Die Funktion getch() liesst den 
    # gedrueckte Buchstabe ein und uebergibt diesen an die 
    # Variablechar. So kann mit der Variable char weiter 
    # gearbeitet werden.
    #char = getch()
    char = ""
   # Das Roboter-Auto faehrt vorwaerts wenn der Anwender die 
   # Taste "w" drueckt.
    if(char == "w" or TcpServer.Direction == "UP"):
        # das Roboter-Auto beschleunigt in Schritten von 10% 
        # mit jedem Tastendruck des Buchstaben "w" bis maximal 
        # 100%. Dann faehrt es maximal schnell vorwaerts.
        speedleft = speedleft + 0.1
        speedright = speedright + 0.1

        if speedleft > 1:
            speedleft = 1
        if speedright > 1:
            speedright = 1
        # Dem Programm L298NHBridge welches zu beginn  
        # importiert wurde wird die Geschwindigkeit fuer 
        # die linken und rechten Motoren uebergeben.
        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        TcpServer.setDirection0()
        printscreen()

    # Das Roboter-Auto faehrt rueckwaerts wenn die Taste "s" 
    # gedrueckt wird.
    if(char == "s" or TcpServer.Direction == "DOWN"):
        # das Roboter-Auto bremst in Schritten von 10% 
        # mit jedem Tastendruck des Buchstaben "s" bis maximal 
        # -100%. Dann faehrt es maximal schnell rueckwaerts.
        speedleft = speedleft - 0.1
        speedright = speedright - 0.1

        if speedleft < -1:
            speedleft = -1
        if speedright < -1:
            speedright = -1
            
        # Dem Programm L298NHBridge welches zu beginn  
        # importiert wurde wird die Geschwindigkeit fuer 
        # die linken und rechten Motoren uebergeben.      
        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        TcpServer.setDirection0()
        printscreen()

        # mit dem druecken der Taste "q" werden die Motoren angehalten
    if(char == "q" or TcpServer.Direction == "STOP"):
        speedleft = 0
        speedright = 0
        HBridge.setMotorLeft(0)
        HBridge.setMotorRight(0)
        printscreen()

    # Mit der Taste "d" lenkt das Auto nach rechts bis die max/min
    # Geschwindigkeit der linken und rechten Motoren erreicht ist.
    if(char == "d" or TcpServer.Direction == "RIGHT"):      
        speedright = speedright - 0.1
        speedleft = speedleft + 0.1
        
        if speedright < -1:
            speedright = -1
        
        if speedleft > 1:
            speedleft = 1
        
        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        TcpServer.setDirection0()
        printscreen()
        
    # Mit der Taste "a" lenkt das Auto nach links bis die max/min
    # Geschwindigkeit der linken und rechten Motoren erreicht ist.
    if(char == "a" or TcpServer.Direction == "LEFT"):
        speedleft = speedleft - 0.1
        speedright = speedright + 0.1
            
        if speedleft < -1:
            speedleft = -1
        
        if speedright > 1:
            speedright = 1
        
        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        TcpServer.setDirection0()
        printscreen()


        # Mit der Taste "x" wird die Endlosschleife beendet 
        # und das Programm wird ebenfalls beendet. Zum Schluss wird 
        # noch die Funktion exit() aufgerufen die die Motoren stoppt.
    if(char == "x"):
        HBridge.setMotorLeft(0)
        HBridge.setMotorRight(0)
        HBridge.exit()
        print("Program Ended")
        break
   
    # Die Variable char wird pro Schleifendurchlauf geleert. 
    # Das ist notwendig um weitere Eingaben sauber zu übernehmen.
    char = ""
