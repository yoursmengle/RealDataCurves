# -*- coding: gb2312 -*-
from socket import *
from pyqtgraph.Qt import QtCore, QtGui
from dataConfig import *
import os
import struct
from math import sin
from time import sleep
import dataConfig
import csv
import numpy as np



class testSendThread(QtCore.QThread):
    HOST = '127.0.0.1'
    PORT = dataConfig.cfgRecvPort
    SERVER = (HOST, PORT)
    f_pause = False
    csvfile = r'inputdata1.csv'

    def __init__(self):
        super().__init__()
        self.s = socket(AF_INET, SOCK_DGRAM)
        self.s.connect(self.SERVER)

    def pause(self):
        self.f_pause = True

    def resume(self):
        self.f_pause = False

    def set_datafile(self, csvfile):
        self.csvfile = csvfile

    def run(self):
        serial = 0
        angle = 0.01
        num_float = dataConfig.cfgDataNumber
        length = num_float * 4;
       
        data = np.loadtxt(self.csvfile, str, delimiter=',', skiprows = 1)
        (rows, cols) = data.shape 
        if cols < num_float:
            print('csv file format error')
            return
        
        for row in range(0,rows):
            if self.f_pause :
                continue

            serial = serial + 1
            if serial > 255:
                serial = 0

            # ! 网络字节序，2B：两个无符号byte类型，H：一个无符号short型
            message = struct.pack("!2BH", 0xaa, serial, length)
            for i in range(0, num_float):
                try:
                    fdata = float(data[row,i])*float(datascale[i])
                except:
                    continue
                if i == 0 or i== 13 or i==20:
                    fdata = 0.0
                temp_str = struct.pack("!f", fdata)  # float
                message = message + temp_str
                self.s.sendall(message)
                #sleep(0.00001)      
             

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys

    testsend = testSendThread()
    testsend.start()

    app = QtGui.QApplication([])
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
