#!/usr/bin/python
import smbus
import math
import time

class GYRO():
    # Register
    def __init__(self):
        self.power_mgmt_1 = 0x6b
        self.power_mgmt_2 = 0x6c
        self.bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
        self.address = 0x68       # via i2cdetect
    
    def read_byte(self,reg):
        return self.bus.read_byte_data(self.address, reg)
    
    def read_word(self,reg):
        h = self.bus.read_byte_data(self.address, reg)
        l = self.bus.read_byte_data(self.address, reg+1)
        value = (h << 8) + l
        return value
    
    def read_word_2c(self,reg):
        val = self.read_word(reg)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val
    
    def dist(self,a,b):
        return math.sqrt((a*a)+(b*b))
    
    def get_y_rotation(self,x,y,z):
        radians = math.atan2(x, self.dist(y,z))
        return -math.degrees(radians)
    
    def get_x_rotation(self,x,y,z):
        radians = math.atan2(y, self.dist(x,z))
        return math.degrees(radians)
    
    def request(self):
    
        # Aktivieren, um das Modul ansprechen zu koennen
        self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)
        
        print("Gyroskop")
        print("--------")
        
        gyroskop_xout = self.read_word_2c(0x43)
        gyroskop_yout = self.read_word_2c(0x45)
        gyroskop_zout = self.read_word_2c(0x47)
        
        # print("gyroskop_xout: ", ("%5d" % gyroskop_xout), " skaliert: ", (gyroskop_xout / 131))
        # print("gyroskop_yout: ", ("%5d" % gyroskop_yout), " skaliert: ", (gyroskop_yout / 131))
        # print("gyroskop_zout: ", ("%5d" % gyroskop_zout), " skaliert: ", (gyroskop_zout / 131))
        
        self.gyroskop_xout_skaliert = gyroskop_xout / 131
        self.gyroskop_yout_skaliert = gyroskop_yout / 131
        self.gyroskop_zout_skaliert = gyroskop_zout / 131

        # print()
        # print("Beschleunigungssensor")
        # print("---------------------")
        
        beschleunigung_xout = self.read_word_2c(0x3b)
        beschleunigung_yout = self.read_word_2c(0x3d)
        beschleunigung_zout = self.read_word_2c(0x3f)
        
        self.beschleunigung_xout_skaliert = beschleunigung_xout / 16384.0
        self.beschleunigung_yout_skaliert = beschleunigung_yout / 16384.0
        self.beschleunigung_zout_skaliert = beschleunigung_zout / 16384.0
        
        # print("beschleunigung_xout: ", ("%6d" % beschleunigung_xout), " skaliert: ", beschleunigung_xout_skaliert)
        # print("beschleunigung_yout: ", ("%6d" % beschleunigung_yout), " skaliert: ", beschleunigung_yout_skaliert)
        # print("beschleunigung_zout: ", ("%6d" % beschleunigung_zout), " skaliert: ", beschleunigung_zout_skaliert)
        
        # print("X Rotation: " , self.get_x_rotation(beschleunigung_xout_skaliert, beschleunigung_yout_skaliert, beschleunigung_zout_skaliert))
        # print("Y Rotation: " , self.get_y_rotation(beschleunigung_xout_skaliert, beschleunigung_yout_skaliert, beschleunigung_zout_skaliert))

    def json(self):
        data = {'X' : self.gyroskop_xout_skaliert,
                'Y' : self.gyroskop_yout_skaliert,
                'Z' : self.gyroskop_zout_skaliert,
                'Beschleunigung' : {
                    'X' : self.beschleunigung_xout_skaliert,
                    'Y' : self.beschleunigung_yout_skaliert,
                    'Z' : self.beschleunigung_zout_skaliert,
                }
                }
        return data