# coding=utf-8
import serial  # 导入模块

try:
    # 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
    portx = "COM7"
    # 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
    bps = 38400
    # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
    timex = 5
    # 打开串口，并得到串口对象
    ser = serial.Serial(portx, bps, timeout=timex)

    # 写数据
    result = ser.write("TestUart".encode("ascii"))
    print("写总字节数:", result)
    response = ser.readall()
    print ("读取的字节为:",response)
    ser.close()  # 关闭串口

except Exception as e:
    print("---异常---：", e)
