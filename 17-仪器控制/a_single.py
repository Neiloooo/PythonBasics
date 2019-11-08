# coding=utf-8
import os
import sys
import urllib

if sys.getdefaultencoding() != "gbk":
    reload(sys)
    sys.setdefaultencoding("gbk")
# 对准格式


'''
Created on 2019-7-26
N5172B信号源
@author: liushuo
'''

import visa
import time

# 频率
Freq = 5830000000
# # 衰减
# Amptd_offset = 2
# 调试深度
depth = 80


# # 功率(幅度值=原始幅度值+线损(衰减))
# amptd_val = -38
# 连接源
# TCPIP0 ='TCPIP0::222.255.255.221::5025::SOCKET'


class signalSource(object):
    # def __init__(self, initParam): 这里单独测试,先把initParam参数去掉
    def __init__(self):
        self.rm = visa.ResourceManager()
        self.N5172B = self.rm.open_resource('TCPIP0::222.255.255.221::5025::SOCKET', write_termination='\n')
        # if 0 != ret:
        #     self.N5172B.close()
        #     self.rm.close()
        #     raise Exception("Can not connect signalSource!")
        # else:
        #     print ("signalSource  connect success!")

    def initRescource(self):
        self.N5172B.read_termination = '\n'
        self.N5172B.write("*RST")

    def open(self):
        # 大概是锁吧
        self.N5172B.write('*RCL %d,%d' % (60, 0))
        # 设置频率
        self.N5172B.write(':SOURce:FREQuency:CW %d' % (Freq))
        # # #衰减(线损)(不用)
        # self.N5172B.write(':SOURce:POWer:LEVel:IMMediate:OFFSet %G' % (Amptd_offset))
        # 设置ask
        self.N5172B.write(":SOURce:RADio:CUSTom:MODulation:TYPE %s" % ("ASK"))
        # 设置深度
        self.N5172B.write((':SOURce:RADio:CUSTom:MODulation:ASK:DEPTh %G' % (depth)))
        # 设置波形
        self.N5172B.write(":SOURce:RADio:CUSTom:FILTer %s" % ("RECTangle"))
        # 设置速率 暂时设置为112
        self.N5172B.write("SOURce:RADio:CUSTom:SRATe %3lf" % (28000))
        # 打开文件
        self.N5172B.write(":SOURce:RADio:CUSTom:DATA %s" % ("\"/USER/BIT/14KHZ\""))
        # # 打开模式
        self.N5172B.write(":SOURce:RADio:CUSTom:STATe %d" % (1))
        # 设置成single
        self.N5172B.write(':SOURce:RADio:CUSTom:TRIGger:TYPE %s' % ('SINGle'))
        # 设置成TRIGger
        self.N5172B.write(":SOURce:RADio:CUSTom:TRIGger:TYPE:CONTinuous:TYPE %s" % ("TRIGger"))
        # 设置成bus
        self.N5172B.write(':SOURce:RADio:CUSTom:TRIGger:SOURce %s' % ('BUS'))

    def send_waken_signal(self, amptd_val, num):
        # 设置幅度值
        self.N5172B.write(':SOURce:POWer:LEVel:IMMediate:AMPLitude %G' % (amptd_val))
        self.N5172B.write(":OUTPut:STATe %d" % (1))
        # 发送开始
        print "run...."
        # 发送次数
        for i in range(1, num):
            self.N5172B.write('*TRG')
            time.sleep(0.1)
            print "==>count %d " % (i)

    def close(self):
        self.N5172B.write(":OUTPut:STATe %d" % (0))
        self.N5172B.close()
        self.rm.close()

    # 查询
    # preamble_string = N5172B.query(":SOURce:RADio:CUSTom:TRIGger:SOURce?")
    # print preamble_string


if __name__ == "__main__":
    a = signalSource()
    a.initRescource()
    a.open()
    a.send_waken_signal(-10, 10)
    a.close()
