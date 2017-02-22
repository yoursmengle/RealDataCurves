# -*- coding: utf-8 -*-
"""
UDP receive Thread
Author: jhzhou
Date: 2017-02-21
"""
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import socket
from dataConfig import *  
from ctypes import *
import struct
import time
import os

class udpRecvThread(QtCore.QThread):
    ptr = 0  #全局数据指针，保存最新的一组数据后加一
    saveData = False   #是否保存数据到文件
    debug = False        #是否输出调试
    def __init__(self):
        super().__init__()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = ''
        self.s.bind((host, cfgRecvPort)) 
        self.allData = np.empty(cfgDataNumber*cfgSavePoints).reshape(cfgDataNumber,cfgSavePoints )         #文件名的时间是【最后】一组数据的接收时间
        if not os.path.exists(cfgSaveFileDir):
            os.mkdir(cfgSaveFileDir)
    
    def startSave(self):
        self.saveData = True
    
    def stopSave(self):
        self.saveData = False
    
    def enableDebug(self):
        self.debug = True
    
        
    def run(self):
        lenRecvBuf = cfgDataNumber*4+20
        while 1:
            message, address = self.s.recvfrom(lenRecvBuf)
            if  self.proc_message(message)== False :  #处理接收到数据，保存到np二维数组（allData）
                continue
            self.ptr +=1
            #数据缓冲区满了，数据指针归零。如果需要，将波形保存到文件
            if self.ptr>=cfgSavePoints: 
                if self.saveData: #保存数据到文件
                    filename = cfgSaveFileDir+'curData_float_'+time.strftime("%Y%m%d_%H%M%S")
                    np.save(filename,  self.allData)
                self.ptr = 0

    def proc_message(self, message):
        str_len = len(message)
        r=dataStructHead()
        headLen = sizeof(dataStructHead)
        structLen = headLen+cfgDataNumber*4
        if str_len < structLen:  #数据总长不符，返回错误
            return False
        
        memmove(addressof(r), message[:headLen], headLen)
        if r.uHead !=0xaa:
            return  False  #帧头不符，返回错误
        if r.uLen+4 != structLen:
            return  False  #长度不符，返回错误
    
        message = message[headLen:]  #去掉帧头
        for i in range(cfgDataNumber):
            self.allData[i, self.ptr] = struct.unpack("!f", message[i*4:(i+1)*4])[0]
        return True


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    udp = udpRecvThread()
    udp.startSave()
    udp.start()
    
    app = QtGui.QApplication([])
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()   
