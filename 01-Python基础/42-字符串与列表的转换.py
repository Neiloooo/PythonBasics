# coding=utf-8
idcodeList = ["F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "FA", "FB", "FC", "FD",
              "FE"]


def cmdFormatToHexStr(cmdStr):
    # 从命令字串转换成普通Hex字符串，即去掉Ox头
    return str("".join(map(lambda x: x.replace("0x", ""), cmdStr.split(" "))))


def SixToTen(lit):
    # 16进制转换成10进制
    list1 = []
    for i in lit:
        i = int(i, 16)
        list1.append(i)
    return list1


def SixToTenNew(lit):
    # 16进制转换成10进制
    list1 = []
    for i in lit:
        i = int(str(i), 16)
        list1.append(i)
    return list1


'''
10进制转换成16
'''


def TO_Formt_HEX(msg):
    list1 = []
    for i in msg:
        i = cmdFormatToHexStr(hex(i)).upper()
        list1.append(i)
    return list1


# 16进制转换
# D0-DF
a = "D0"
b = "DF"
a = int(a, 16)
b = int(b, 16)
list2 = []
for i in range(a, b):
    list2.append(i)
list3 = TO_Formt_HEX(list2)
