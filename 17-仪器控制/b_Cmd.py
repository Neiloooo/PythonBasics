# coding=utf-8
from __future__ import print_function
import serial  # 导入模块
import a_single

'''
Created on 2019-7-26
控制信号源唤醒OBU
@author: liushuo
'''

# 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
portx = "COM7"
# 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
bps = 38400
# 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
timex = 5


# 串口通信
class SerialCommunication(object):

    def __init__(self):
        try:
            self.ser = serial.Serial(portx, bps, timeout=timex)
        except Exception as e:
            print("--串口连接失败---：", e)

    def initRescource(self):
        pass

    def WriteAndReadAll(self, StringCMD):
        try:
            # 写数据
            result = self.ser.write(StringCMD.encode("ascii"))
            print("Write : ", result)
            self.responseCMD = self.ser.readall()
            return self.responseCMD


        except Exception as e:
            print("--串口发送或接收失败---：", e)

    def assertResultOk1(self, expect):
        print(expect)
        print(self.responseCMD)
        if expect != None and self.responseCMD is not None and self.responseCMD == expect:
            return True
        return False

    def closeSerial(self):
        try:
            self.ser.close()  # 关闭串口
        except Exception as e:
            print("--串口关闭失败---：", e)


if __name__ == "__main__":
    # 唤醒一次,要求:从-10到3一直唤醒
    # 获取信号源对象
    S = a_single.signalSource()
    # 获取串口对象
    a = SerialCommunication()
    # 清空唤醒状态
    a.WriteAndReadAll("IfObuWakeUp")
    S.initRescource()
    S.open()

    # 唤醒功率
    # amptd_val = [-30, -20, -10]
    flage = False

    # 唤醒频率三人组
    start = -30
    end = 0
    length = 1 #步长


    for i in range(start, end, length):
        S.send_waken_signal(i, 10)
        print("信号源发送信号成功")
        # 测试是否唤醒成功
        response = a.WriteAndReadAll("IfObuWakeUp")
        print("串口发送指令成功")
        if a.assertResultOk1("TWOK\r\n"):
            print("唤醒成功,唤醒功率为 :  %d" % (i))
            flage = True
            break
        else:
            print("%d 唤醒失败" % (i))

    # print(flage)
    # if flage:
    #     print("恭喜你唤醒成功了")
    # else:
    #     print("对不起没有能唤醒OBU的功率")

    S.close()
    a.closeSerial()
