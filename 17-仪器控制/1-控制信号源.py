# coding: utf-8
# !/usr/bin/env python
# coding: utf-8
import os
import sys
import urllib

if sys.getdefaultencoding() != "gbk":
    reload(sys)
    sys.setdefaultencoding("gbk")
import visa
import time

# 频率
Freq = 5830000000
# # 衰减
Amptd_offset = 2
# 调试深度
depth = 80
# 功率(幅度值=原始幅度值+线损(衰减))
amptd_val = -38

rm = visa.ResourceManager()
N5172B = rm.open_resource("TCPIP0::222.255.255.221::5025::SOCKET", write_termination='\n')
N5172B.read_termination = '\n'
N5172B.write("*RST")
# 大概是锁吧
N5172B.write('*RCL %d,%d' % (60, 0))
# N5172B.write(':SOURce:FREQuency:CW %d' % (Freq))  # 频率
# N5172B.write(':SOURce:POWer:LEVel:IMMediate:OFFSet %G' % (Amptd_offset))  # 衰减
# N5172B.write(':SOURce:POWer:LEVel:IMMediate:AMPLitude %G' % (amptd_val))  # 调试幅度
# N5172B.write(':SOURce:RADio:CUSTom:MODulation:ASK:DEPTh %G' % (depth))  # 深度
# # 写方法,写参数的
# N5172B.write(':SOURce:RADio:CUSTom:TRIGger:TYPE %s' % ('SINGle'))  # 触发方式
# N5172B.write(':SOURce:RADio:CUSTom:TRIGger:SOURce %s' % ('BUS'))  # 源头
# N5172B.write(':OUTPut:STATe %d' % (1))
# 修改的张文硕的命令

# 设置频率
N5172B.write(':SOURce:FREQuency:CW %d' % (Freq))
# 设置幅度值
N5172B.write(':SOURce:POWer:LEVel:IMMediate:AMPLitude %G' % (amptd_val))
# # #衰减(线损)(不用)
# N5172B.write(':SOURce:POWer:LEVel:IMMediate:OFFSet %G' % (Amptd_offset))

# 设置ask
N5172B.write(":SOURce:RADio:CUSTom:MODulation:TYPE %s" % ("ASK"))
# 设置深度
N5172B.write((':SOURce:RADio:CUSTom:MODulation:ASK:DEPTh %G' % (depth)))
# 设置波形
N5172B.write(":SOURce:RADio:CUSTom:FILTer %s" % ("RECTangle"))
# 设置速率 暂时设置为112
N5172B.write("SOURce:RADio:CUSTom:SRATe %3lf" % (112000))
# 打开文件
N5172B.write(":SOURce:RADio:CUSTom:DATA %s" % ("\"/USER/BIT/14KHZ\""))
# # 打开模式
N5172B.write(":SOURce:RADio:CUSTom:STATe %d" % (1))
# 设置成single
N5172B.write(':SOURce:RADio:CUSTom:TRIGger:TYPE %s' % ('SINGle'))
# 设置成TRIGger
N5172B.write(":SOURce:RADio:CUSTom:TRIGger:TYPE:CONTinuous:TYPE %s" % ("TRIGger"))
# 设置成bus
N5172B.write(':SOURce:RADio:CUSTom:TRIGger:SOURce %s' % ('BUS'))

# 查询某项数据的参数


# preamble_string = N5172B.query(":SOURce:RADio:CUSTom:TRIGger:SOURce?")
# print preamble_string

print "run...."
for i in range(1, 20):
    N5172B.write('*TRG')
    time.sleep(0.1)
    print "==>count %d " % (i)

N5172B.close()
rm.close()
