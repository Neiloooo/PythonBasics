# coding=utf-8
def hexStrToSerialCmdFormat(hexStr):
    # 从16进制字符串转换成串口命令格式，即0x11 0x33 ....
    return str(" ".join(["0x" + hexStr[2 * i:2 * i + 2] for i in range(len(hexStr) / 2)]))


def cmdFormatToHexStr(cmdStr):
    # 从命令字串转换成普通Hex字符串，即去掉Ox头
    return str("".join(map(lambda x: x.replace("0x", ""), cmdStr.split(" "))))


a = "0xc1 0x02 0x55 0x44 0xff 0x90"
res = list(filter(None, a.split(" ")))
list = []
for i in res:
    i = cmdFormatToHexStr(i)
    i=int(i, 16)
    list.append(i)
print list[0]
print list[2]

# for i in range(0, 96,16):
#     a = '{0:02X}'.format(int(i))
#     a = hexStrToSerialCmdFormat(str(a))
#     print a
