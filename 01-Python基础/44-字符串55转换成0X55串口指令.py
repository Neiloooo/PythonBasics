# coding=utf-8
def hexStrToSerialCmdFormat(hexStr):
    # 从16进制字符串转换成串口命令格式，即0x11 0x33 ....
    return str(" ".join(["0x" + hexStr[2 * i:2 * i + 2] for i in range(len(hexStr) / 2)]))


def cmdFormatToHexStr(cmdStr):
    # 从命令字串转换成普通Hex字符串，即去掉Ox头
    return str("".join(map(lambda x: x.replace("0x", ""), cmdStr.split(" "))))


A = "55555555000000000000000000010000"
B = hexStrToSerialCmdFormat(A)
t = B
res = list(filter(None, t.split(" ")))
list2 = []
for i in res:
    i = hexStrToSerialCmdFormat(cmdFormatToHexStr(i))
    i = int(i, 16)
    i = hexStrToSerialCmdFormat('{0:02X}'.format(int(i)))
    # i = hex(i)
    list2.append(i)

print list2[0]
print list2[3]
print list2[4]
