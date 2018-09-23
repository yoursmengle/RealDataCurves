# -*- coding: gb2312 -*-
from socket import *
from pyqtgraph.Qt import QtCore, QtGui
from dataConfig import *
import os
import struct
from math import sin
from time import sleep
import dataConfig



class testSendThread(QtCore.QThread):
    HOST = '127.0.0.1'
    PORT = dataConfig.cfgRecvPort
    SERVER = (HOST, PORT)

    def __init__(self):
        super().__init__()
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(SERVER)
        serial = 0
        angle = 0.01
        num_float = dataConfig.cfgDataNumber

    def run(self):
        while True:
            serial = serial + 1
            if serial > 255:
                serial = 0
            length = num_float * 4;

            # ! 网络字节序，2B：两个无符号byte类型，H：一个无符号short型
            message = struct.pack("!2BH", 0xaa, serial, length)

            angle = angle + 0.01;
            if angle > 359.99:
                angle = 0
            for i in range(0, num_float):
                fData = sin(angle * 3.14159 * 2 / 360 + 3.14 / 18 * i)
                temp_str = struct.pack("!f", fData)  # float
                message = message + temp_str

            s.sendall(message)
            sleep(0.001)


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys

    udp = testSendThread()
    udp.start()

    app = QtGui.QApplication([])
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
