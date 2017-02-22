# -*- coding: utf-8 -*-
"""
Config  file of UDP data
Author: jhzhou
Date: 2017-02-21
"""
from ctypes import *

cfgRecvPort = 15600   #本主机通过UDP接收数据的端口号
cfgSavePoints = 1000000     #每个数据波形的缓存点数
cfgSaveFileDir = 'D:/curvesData/'


#数据名称，与实际的数据一一对应
cfgDataNames = [ '机械转速', 
            '电磁转速', 
            '电流d', 
            '电流q', 
            '电压d', 
            '电压q', 
            '机械角度', 
            '电磁角度', 
            '绝对位置', 
            '保留1', 
            '保留2', 
            '保留3'
            ]
                            
cfgDataNumber = len(cfgDataNames)

class dataStructHead(BigEndianStructure):    #The datas are from network ( BigEndian)
    _fields_=[('uHead', c_ubyte),    #帧头，固定为0x55
                ('uSerial', c_ubyte),   #序列号，每帧自动加一
                ('uLen', c_ushort)      #后面数据的总字节数，= 数据个数*4
                ]
#帧头后面跟着实际的数据，格式为单精度浮点（32位）
