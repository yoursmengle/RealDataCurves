# -*- coding: utf-8 -*-
"""
Displayer of Real Data from UDP
Author: jhzhou
Date: 2017-02-21
"""
import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
from myPlotWidget import *
from myQTableWidget import *
from dataConfig import *
import time

class myMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.initWindow();    
        
    def initWindow(self):
        self.setWindowTitle('Curves displayer by jhzhou')
        self.resize(1680,1024)
        cw = QtGui.QWidget() 
        self.setCentralWidget(cw)
        mh = QtGui.QHBoxLayout()
        cw.setLayout(mh)
        
        self.pw = myPlotWidget(curvesNum = 8)
        
        #创建曲线下面的说明
        g8 =QtGui.QGroupBox('曲线颜色说明')
        self.nameCurve = [(QtGui.QLabel('未设置')), (QtGui.QLabel('未设置')), (QtGui.QLabel('未设置')), (QtGui.QLabel('未设置')), (QtGui.QLabel('未设置')), (QtGui.QLabel('未设置')), (QtGui.QLabel('未设置')),(QtGui.QLabel('未设置'))]
        h8=QtGui.QHBoxLayout()
        self.txtCurve1 = QtGui.QPushButton('曲线1')
        self.txtCurve2 = QtGui.QPushButton('曲线2')
        self.txtCurve3 = QtGui.QPushButton('曲线3')
        self.txtCurve4 = QtGui.QPushButton('曲线4')
        self.txtCurve5 = QtGui.QPushButton('曲线5')
        self.txtCurve6 = QtGui.QPushButton('曲线6')
        self.txtCurve7 = QtGui.QPushButton('曲线7')
        self.txtCurve8 = QtGui.QPushButton('曲线8')
        
        #设置颜色
        cPen = QtGui.QPalette()
        self.txtCurve1.setAutoFillBackground(True)
        self.txtCurve2.setAutoFillBackground(True)
        self.txtCurve3.setAutoFillBackground(True)
        self.txtCurve4.setAutoFillBackground(True)
        self.txtCurve5.setAutoFillBackground(True)
        self.txtCurve6.setAutoFillBackground(True)
        self.txtCurve7.setAutoFillBackground(True)
        self.txtCurve8.setAutoFillBackground(True)
        self.nameCurve[0].setAutoFillBackground(True)
        self.nameCurve[1].setAutoFillBackground(True)
        self.nameCurve[2].setAutoFillBackground(True)
        self.nameCurve[3].setAutoFillBackground(True)
        self.nameCurve[4].setAutoFillBackground(True)
        self.nameCurve[5].setAutoFillBackground(True)
        self.nameCurve[6].setAutoFillBackground(True)
        self.nameCurve[7].setAutoFillBackground(True)
        
        #设置字体
        self.txtCurve1.setFont(QtGui.QFont("song", 18, QtGui.QFont.Bold))
        self.txtCurve2.setFont(QtGui.QFont("song", 18, QtGui.QFont.Bold))
        self.txtCurve3.setFont(QtGui.QFont("song", 18, QtGui.QFont.Bold))
        self.txtCurve4.setFont(QtGui.QFont("song", 18, QtGui.QFont.Bold))
        self.txtCurve5.setFont(QtGui.QFont("song", 18, QtGui.QFont.Bold))
        self.txtCurve6.setFont(QtGui.QFont("song", 18, QtGui.QFont.Bold))
        self.txtCurve7.setFont(QtGui.QFont("song", 18, QtGui.QFont.Bold))
        self.txtCurve8.setFont(QtGui.QFont("song", 18, QtGui.QFont.Bold))
        curvesNum = self.pw.getCurvesNumber()
        for i in range(curvesNum):
            self.nameCurve[i].setFont(QtGui.QFont("song", 18, QtGui.QFont.Bold))
        
        
        cPen.setColor(QtGui.QPalette.WindowText,QtGui.QColor(255, 0, 0))
        cPen.setColor(QtGui.QPalette.Window,QtCore.Qt.black)
        self.txtCurve1.setPalette(cPen)
        self.nameCurve[0].setPalette(cPen)
        
        cPen.setColor(QtGui.QPalette.WindowText,QtGui.QColor(0, 255, 0))
        cPen.setColor(QtGui.QPalette.Window,QtCore.Qt.black)
        self.txtCurve2.setPalette(cPen)
        self.nameCurve[1].setPalette(cPen)
         
        cPen.setColor(QtGui.QPalette.WindowText,QtGui.QColor(0, 0, 255))
        cPen.setColor(QtGui.QPalette.Window,QtCore.Qt.black)
        self.txtCurve3.setPalette(cPen)
        self.nameCurve[2].setPalette(cPen)
         
        cPen.setColor(QtGui.QPalette.WindowText,QtGui.QColor(255, 255, 0))
        cPen.setColor(QtGui.QPalette.Window,QtCore.Qt.black)
        self.txtCurve4.setPalette(cPen)
        self.nameCurve[3].setPalette(cPen)
         
        cPen.setColor(QtGui.QPalette.WindowText,QtGui.QColor(0, 255, 255))
        cPen.setColor(QtGui.QPalette.Window,QtCore.Qt.black)
        self.txtCurve5.setPalette(cPen)
        self.nameCurve[4].setPalette(cPen)
        
        cPen.setColor(QtGui.QPalette.WindowText,QtGui.QColor(255, 0, 255))
        cPen.setColor(QtGui.QPalette.Window,QtCore.Qt.black)
        self.txtCurve6.setPalette(cPen)
        self.nameCurve[5].setPalette(cPen)
        
        cPen.setColor(QtGui.QPalette.WindowText,QtGui.QColor(255, 255, 255))
        cPen.setColor(QtGui.QPalette.Window,QtCore.Qt.black)
        self.txtCurve7.setPalette(cPen)
        self.nameCurve[6].setPalette(cPen)
        
        cPen.setColor(QtGui.QPalette.WindowText,QtGui.QColor(128, 128, 0))
        cPen.setColor(QtGui.QPalette.Window,QtCore.Qt.black)
        self.txtCurve8.setPalette(cPen)
        self.nameCurve[7].setPalette(cPen)
        
        h8.addStretch(1)
        h8.addWidget(self.txtCurve1)
        h8.addWidget(self.nameCurve[0])
        h8.addStretch(2)
        h8.addWidget(self.txtCurve2)
        h8.addWidget(self.nameCurve[1])
        h8.addStretch(2)
        h8.addWidget(self.txtCurve3)
        h8.addWidget(self.nameCurve[2])
        h8.addStretch(2)
        h8.addWidget(self.txtCurve4)
        h8.addWidget(self.nameCurve[3])
        h8.addStretch(2)
        h8.addWidget(self.txtCurve5)
        h8.addWidget(self.nameCurve[4])
        h8.addStretch(2)
        h8.addWidget(self.txtCurve6)
        h8.addWidget(self.nameCurve[5])
        h8.addStretch(2)
        h8.addWidget(self.txtCurve7)
        h8.addWidget(self.nameCurve[6])
        h8.addStretch(2)
        h8.addWidget(self.txtCurve8)
        h8.addWidget(self.nameCurve[7])
        h8.addStretch(1)
        g8.setLayout(h8)
        
        #创建曲线区下面的操作按钮部分
        gCmd =QtGui.QGroupBox('控制面板')
        h=QtGui.QHBoxLayout()
        self.saveChk = QtGui.QCheckBox('自动保存')
        self.saveChk.setChecked(True)  #启动时缺省自动保存
        self.saveChk.setFont(QtGui.QFont("song", 18, QtGui.QFont.Bold))
        self.runButton = QtGui.QPushButton('暂停')
        self.runButton.setFont(QtGui.QFont("song", 18, QtGui.QFont.Bold))
        self.clearButton = QtGui.QPushButton('清空')
        self.clearButton.setFont(QtGui.QFont("song", 18, QtGui.QFont.Bold))
        self.openFileButton = QtGui.QPushButton('打开文件')
        self.openFileButton.setFont(QtGui.QFont("song", 18, QtGui.QFont.Bold))
        self.saveFileButton = QtGui.QPushButton('手动保存')
        self.saveFileButton.setFont(QtGui.QFont("song", 18, QtGui.QFont.Bold))
        self.quitButton = QtGui.QPushButton('保存退出')
        self.quitButton.setFont(QtGui.QFont("song", 18, QtGui.QFont.Bold))
       
        h.addStretch(6)
        h.addWidget(self.saveChk)
        h.addStretch(2)
        h.addWidget(self.saveFileButton)
        h.addStretch(2)
        h.addWidget(self.openFileButton)
        h.addStretch(2)
        h.addWidget(self.runButton)
        h.addStretch(2)
        h.addWidget(self.clearButton)
        h.addStretch(2)
        h.addWidget(self.quitButton)
        h.addStretch(1)
        gCmd.setLayout(h)
        
        v_left = QtGui.QVBoxLayout()
        v_left.addWidget(self.pw)
        v_left.addWidget(g8)
        v_left.addWidget(gCmd)
        
        #创建右侧的数据显示区
        g0 = QtGui.QGroupBox('数据面板')
        v0 = QtGui.QVBoxLayout()
        #dataTab = QtGui.QTableWidget(20,2)  #创建实时数据表格
        self.dataTab = myQTableWidget()  #创建实时数据表格
           
        v0.addWidget(self.dataTab)
        g0.setLayout(v0)
        
        mh.addLayout(v_left, stretch=4)
        mh.addWidget(g0, stretch=1)        
 
## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    from udpRecv import *
    from PyQt5.QtWidgets import QFileDialog 
    
    cmd_stop = False

    udp = udpRecvThread()
    udp.startSave()
    udp.start()
    app = QtGui.QApplication([])
   
    mw = myMainWindow()
    mw.show()
    
    def update01():
        global cmd_stop
        mw.dataTab.updateData(allData = udp.allData,  ptr=udp.ptr)  #更新表格中的实时数据
        for i in range(mw.pw.curvesNum):
            mw.nameCurve[i].setText(cfgDataNames[mw.dataTab.selected[i]])  #更新各条曲线的名称
    timer01 = QtCore.QTimer()
    timer01.timeout.connect(update01)
    timer01.start(100)
    
    def update02():
        global cmd_stop
        for i in range(mw.pw.curvesNum):
            if mw.dataTab.curveChanged[i] == True :
                mw.pw.setCurve(i, mw.dataTab.selected[i])
                mw.pw.enableCurve(i)
                mw.dataTab.curveChanged[i] = False    

        if cmd_stop:   #停止按钮按下，停止数据刷新
            return
        mw.pw.updateCurves(allData = udp.allData,  ptr=udp.ptr)

    timer02 = QtCore.QTimer()
    timer02.timeout.connect(update02)
    timer02.start(1)
    
    def toggle_curve1():
        if mw.pw.cfgCurve[1, 0] == True:
            mw.pw.disableCurve(0)
        else:
            mw.pw.enableCurve(0)
    mw.txtCurve1.clicked.connect(toggle_curve1)  
    
    def toggle_curve2():
        if mw.pw.cfgCurve[1, 1] == True:
            mw.pw.disableCurve(1)
        else:
            mw.pw.enableCurve(1)
    mw.txtCurve2.clicked.connect(toggle_curve2)  
    
    def toggle_curve3():
        if mw.pw.cfgCurve[1, 2] == True:
            mw.pw.disableCurve(2)
        else:
            mw.pw.enableCurve(2)
    mw.txtCurve3.clicked.connect(toggle_curve3)  
    
    def toggle_curve4():
        if mw.pw.cfgCurve[1, 3] == True:
            mw.pw.disableCurve(3)
        else:
            mw.pw.enableCurve(3)
    mw.txtCurve4.clicked.connect(toggle_curve4)  
    
    def toggle_curve5():
        if mw.pw.cfgCurve[1, 4] == True:
            mw.pw.disableCurve(4)
        else:
            mw.pw.enableCurve(4)
    mw.txtCurve5.clicked.connect(toggle_curve5)  
    
    def toggle_curve6():
        if mw.pw.cfgCurve[1, 5] == True:
            mw.pw.disableCurve(5)
        else:
            mw.pw.enableCurve(5)
    mw.txtCurve6.clicked.connect(toggle_curve6)  
    
    def toggle_curve7():
        if mw.pw.cfgCurve[1, 6] == True:
            mw.pw.disableCurve(6)
        else:
            mw.pw.enableCurve(6)
    mw.txtCurve7.clicked.connect(toggle_curve7)  
    
    def toggle_curve8():
        if mw.pw.cfgCurve[1, 7] == True:
            mw.pw.disableCurve(7)
        else:
            mw.pw.enableCurve(7)
    mw.txtCurve8.clicked.connect(toggle_curve8)  
        
    def run_clicked():
        global cmd_stop
        if cmd_stop :
            cmd_stop = False
            mw.runButton.setText('暂停')
        else:
            cmd_stop = True
            mw.runButton.setText('运行')
    mw.runButton.clicked.connect(run_clicked)
        
    def clear_clicked():
        udp.ptr = 0
    mw.clearButton.clicked.connect(clear_clicked)
    
    def open_clicked():
        global cmd_stop
        fileName, filetype = QFileDialog.getOpenFileName(  
                                    caption = "选取文件",  
                                    directory = cfgSaveFileDir,  
                                    filter = "Data Files (*.npy)"
                                    )
        if fileName == '':
            return
        cmd_stop = True    #打开历史文件时关闭实时显示
        mw.runButton.setText('运行')
        hisData = np.load(fileName)
        mw.pw.updateCurves(allData = hisData,  ptr=hisData.shape[1])
    mw.openFileButton.clicked.connect(open_clicked)

    def save_clicked():
        fileName, filetype = QFileDialog.getSaveFileName(  
                                    caption = "保存文件",  
                                    directory = cfgSaveFileDir,  
                                    filter = "Data Files (*.npy)"
                                    )  
        if fileName == '':
            return
        np.save(fileName, udp.allData[0:cfgDataNumber, 0:udp.ptr])
    mw.saveFileButton.clicked.connect(save_clicked)
    
    def quit_clicked():
        fileName = cfgSaveFileDir+'curData_float_'+time.strftime("%Y%m%d_%H%M%S")
        np.save(fileName, udp.allData[0:cfgDataNumber, 0:udp.ptr])
        mw.hide()
        app.quit()
    mw.quitButton.clicked.connect(quit_clicked)
        
    def saveFileCheck(state):
        if state == QtCore.Qt.Checked:
            udp.startSave()
        else:
            udp.stopSave()
    mw.saveChk.stateChanged.connect(saveFileCheck)

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
