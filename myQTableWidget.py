# -*- coding: utf-8 -*-
"""
Read Data Table  
Author: jhzhou
Date: 2017-02-21
"""

from pyqtgraph.Qt import QtCore, QtGui
from myPlotWidget import  *
from dataConfig import *

class myQTableWidget(QtGui.QTableWidget):
    selected = [0, 1, 2, 3, 4, 5, 6, 7]   #8条曲线是否被选择，
    curveChanged = [True, True, True, True, True, True, True, True]  #曲线变化标志
    def __init__(self, parent=None):
        super().__init__()
        self.initTab();
        
    def initTab(self):
        self.setColumnCount(2)
        self.setRowCount(cfgDataNumber)
        self.setHorizontalHeaderLabels(['名称', '实时值'])
        self.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)  #设置为不可编辑
        self.setAlternatingRowColors(True)  #设置为隔行改变颜色
        for i in range(cfgDataNumber):  #填充数据名称和初始值 0.0
            item=QtGui.QTableWidgetItem(cfgDataNames[i])    
            self.setItem(i,0, item)
            item=QtGui.QTableWidgetItem('%f'%0.0)  
            self.setItem(i,1, item)
        self.createContextMenu()
        
        
    def createContextMenu(self):
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        
        self.contextMenu = QtGui.QMenu(self)
        self.action0 = self.contextMenu.addAction(QtGui.QIcon('255000000.ico.png'), u'设置到曲线1')
        self.action1 = self.contextMenu.addAction(QtGui.QIcon('000255000.ico.png'), u'设置到曲线2')
        self.action2 = self.contextMenu.addAction(QtGui.QIcon('000000255.ico.png'), u'设置到曲线3')
        self.action3 = self.contextMenu.addAction(QtGui.QIcon('255255000.ico.png'), u'设置到曲线4')
        self.action4 = self.contextMenu.addAction(QtGui.QIcon('000255255.ico.png'), u'设置到曲线5')
        self.action5 = self.contextMenu.addAction(QtGui.QIcon('255000255.ico.png'), u'设置到曲线6')
        self.action6 = self.contextMenu.addAction(QtGui.QIcon('255255255.ico.png'), u'设置到曲线7')
        self.action7 = self.contextMenu.addAction(QtGui.QIcon('128128000.ico.png'), u'设置到曲线8')
        
        self.action0.triggered.connect(self.actionHandler1)
        self.action1.triggered.connect(self.actionHandler2)
        self.action2.triggered.connect(self.actionHandler3)
        self.action3.triggered.connect(self.actionHandler4)
        self.action4.triggered.connect(self.actionHandler5)
        self.action5.triggered.connect(self.actionHandler6)
        self.action6.triggered.connect(self.actionHandler7)
        self.action7.triggered.connect(self.actionHandler8)

    def showContextMenu(self, pos):
        self.contextMenu.move(QtGui.QCursor.pos())
        self.contextMenu.show()
    
    def updateData(self, allData,ptr): 
        if ptr ==0 :
            return   
        for i in range(cfgDataNumber):
            item=QtGui.QTableWidgetItem('%f'%allData[i, ptr-1]) 
            self.setItem(i, 1, item) 
    def getSelectedData(self):
        return self.selected
        
    def setCurrDataToCurve(self, curveNo):
        r = self.currentRow()
        if r in self.selected:
            QtGui.QMessageBox.information(self,"温馨提示","所选数据已经被显示。")
            return
        self.selected[curveNo] = r
        self.curveChanged[curveNo] = True

    def actionHandler1(self):
       self.setCurrDataToCurve(0)
    def actionHandler2(self):
       self.setCurrDataToCurve(1)
    def actionHandler3(self):
        self.setCurrDataToCurve(2)
    def actionHandler4(self):
        self.setCurrDataToCurve(3)
    def actionHandler5(self):
        self.setCurrDataToCurve(4)
    def actionHandler6(self):
        self.setCurrDataToCurve(5)
    def actionHandler7(self):
        self.setCurrDataToCurve(6)
    def actionHandler8(self):
        self.setCurrDataToCurve(7)
        

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
    tab = myQTableWidget()
    mw.setCentralWidget(tab)

    mw.show()


    def update():
        tab.updateData(allData = udp.allData,  ptr=udp.ptr)
    timer_curves = QtCore.QTimer()
    timer_curves.timeout.connect(update)
    timer_curves.start(10)    
    

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()       
