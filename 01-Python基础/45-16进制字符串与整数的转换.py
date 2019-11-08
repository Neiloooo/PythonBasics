# coding=utf-8
def hexStrToSerialCmdFormat(hexStr):
    # 从16进制字符串转换成串口命令格式，即0x11 0x33 ....
    return str(" ".join(["0x" + hexStr[2 * i:2 * i + 2] for i in range(len(hexStr) / 2)]))


def str2hex(s):
    odata = 0;
    su = s.upper()
    for c in su:
        tmp = ord(c)
        if tmp <= ord('9'):
            odata = odata << 4
            odata += tmp - ord('0')
        elif ord('A') <= tmp <= ord('F'):
            odata = odata << 4
            odata += tmp - ord('A') + 10
    return odata


b = "aaa"
a = str2hex(b)
print type(a)
print a
