# -*- coding: utf-8 -*-
"""
MultiCurves Displayer
Author: jhzhou
Date: 2017-02-21
"""
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

class myPlotWidget(pg.PlotWidget):
    curvesNum= 8
    penColor = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 255), (128, 128, 0)]
    penBlack = (0, 0, 0)
    cfgCurve = np.array( [(0, 1, 2, 3, 4, 5, 6, 7), (True, True, True, True, True, True, True, True)])   #配置8条曲线，对应的数据序号和是否显示标志
    gCurves =[1, 2, 3, 4, 5, 6, 7, 8]
    def __init__(self, parent=None, curvesNum = 8):
        if curvesNum >= 8:
            curvesNum = 8
        super().__init__()
        self.setDownsampling(mode='peak')
        self.setClipToView(True)
        self.setRange(xRange=[-100, 0])
        self.setLimits(xMax=0)
        self.initCurves(curvesNum)
        
    def initCurves(self, curvesNum):    
        self.curvesNum = curvesNum
        for i in range(curvesNum):
            self.gCurves[i] = self.plot(pen=self.penColor[i])
            
        self.cfgCurve    
        
    def setCurve(self, curNo,  dataNo):
        if dataNo < 0:
            return
        self.cfgCurve[0,curNo] = dataNo   #设置本条曲线对应的数据序号
    def disableCurve(self, curNo):
        self.cfgCurve[1, curNo] = False
        self.gCurves[curNo].setPen(self.penBlack)
    def enableCurve(self, curNo):
        self.cfgCurve[1, curNo] = True
        self.gCurves[curNo].setPen(self.penColor[curNo])
    
    def updateCurves(self, allData, ptr):
        for i in range(self.curvesNum):
            dataIndex = self.cfgCurve[0, i]
            self.gCurves[i].setData(allData[dataIndex][0:ptr])
            self.gCurves[i].setPos(0-ptr, 0)
    def getCurvesNumber(self):
        return self.curvesNum
        
    


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    from udpRecv import *
    
    app = QtGui.QApplication([])

    udp = udpRecvThread()
    udp.startSave()
    udp.start()
    
    mw = QtGui.QMainWindow()
    mw.setWindowTitle('Test multi PlotWidget by jhzhou')
    pw = myPlotWidget()
    mw.setCentralWidget(pw)

    mw.show()


    def update():
        pw.updateCurves(allData = udp.allData,  ptr=udp.ptr)
    timer_curves = QtCore.QTimer()
    timer_curves.timeout.connect(update)
    timer_curves.start(10)    
    

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()       
