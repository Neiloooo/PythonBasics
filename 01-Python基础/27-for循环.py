# coding=utf-8
def hexStrToSerialCmdFormat(hexStr):
    # 从16进制字符串转换成串口命令格式，即0x11 0x33 ....
    return str(" ".join(["0x" + hexStr[2 * i:2 * i + 2] for i in range(len(hexStr) / 2)]))

#
# x = 1
# a = '{0:02X}'.format(int(x))
# a = hexStrToSerialCmdFormat(str(a))
# print a


dataList = [0, 1, 2, 3, 4, 5]
i =1
for dataInfo in dataList:
    i = i + 1
    a = hexStrToSerialCmdFormat(str('{0:02X}'.format(int(i))))
    print a
    print type(a)
    print dataInfo
    if i == 6:
        print "Success"
        break
