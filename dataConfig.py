# -*- coding: utf-8 -*-
"""
Config  file of UDP data
Author: jhzhou
Date: 2017-02-21
"""
import ctypes

cfgRecvPort = 15600   #本主机通过UDP接收数据的端口号
cfgSavePoints = 1000000     #每个数据波形的缓存点数
cfgSaveFileDir = 'D:/curvesData/'


#数据名称，与实际的数据一一对应
cfgDataNames = ['备用', 
            '电流', 
            '平均功率*10', 
            '前泵主压*10', 
            '后泵主压*10', 
            '前泵流量', 
            '后泵流量', 
            '比例阀', 
            '前泵功率*10', 
            '后泵功率*10', 
            '电阻*100', 
            '前泵扭矩', 
            '后泵扭矩', 
            '备用',   ###
            '负载率',
            '需求扭矩',
            '实际扭矩',
            '设定转速',
            '实际转速',
            '燃油率',
            '备用',  ###
            '摩擦扭矩*100', 
            '掉速率*1000'
            ]
                   
datascale = [1,
             1,
             10,
             10,
             10,
             1,
             1,
             1,
             10,
             10,
             100,
             1,
             1,
             1,
             1,
             1,
             1,
             1,
             1,
             1,
             1,
             100,
             1000,             
             ]         
cfgDataNumber = len(cfgDataNames)

class dataStructHead(ctypes.BigEndianStructure):    #The datas are from network ( BigEndian)
    _fields_=[('uHead', ctypes.c_ubyte),    #帧头，固定为0x55
                ('uSerial', ctypes.c_ubyte),   #序列号，每帧自动加一
                ('uLen', ctypes.c_ushort)      #后面数据的总字节数，= 数据个数*4
                ]
#帧头后面跟着实际的数据，格式为单精度浮点（32位）
