# -*- coding: gb2312 -*-
from socket import *
import os
import struct
from math import sin
from time import sleep
import dataConfig


HOST = '127.0.0.1'
PORT = dataConfig.cfgRecvPort

SERVER = (HOST, PORT)

s = socket(AF_INET,SOCK_DGRAM)  
s.connect(SERVER)
serial = 0
angle = 0.01
num_float = dataConfig.cfgDataNumber

while True:  
    serial = serial +1
    if serial > 255 :
        serial = 0
    length = num_float*4;
    
    #! 网络字节序，2B：两个无符号byte类型，H：一个无符号short型
    message = struct.pack("!2BH", 0xaa,serial,length)   

    angle = angle + 0.01;
    if angle >359.99:
        angle = 0
    for i in range(0, num_float):
        fData = sin(angle*3.14159*2/360+3.14/18*i)
        temp_str = struct.pack("!f", fData)  #float
        message = message + temp_str
    
    s.sendall(message)
    sleep(0.001)
 #   print len(message)
 #   print repr(message)
 #   print fData

s.close()  
