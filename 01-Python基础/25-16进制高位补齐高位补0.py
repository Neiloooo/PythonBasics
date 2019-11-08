# coding=utf-8
def hexStrToSerialCmdFormat(hexStr):
    # 从16进制字符串转换成串口命令格式，即0x11 0x33 ....
    return str(" ".join(["0x" + hexStr[2 * i:2 * i + 2] for i in range(len(hexStr) / 2)]))


def cmdFormatToHexStr(cmdStr):
    # 从命令字串转换成普通Hex字符串，即去掉Ox头
    return str("".join(map(lambda x: x.replace("0x", ""), cmdStr.split(" "))))


# list2 = [0x01, 0x02, 0x03, 0x04]
# number = len(list2)
x = 12
print('{0:08X}'.format(int(x)))

# a = 1
# b = 22
# print(format(float(a) / float(b), '.2f'))
#
# l = [1, 2, 3, 4, 5, 4, 3, 2, 1]  # 输入数字到数组中
# # sum(l)/len(l) #求平均数
# print("{:.2f}".format(sum(l) / len(l)))  # 求平均数，保留3位小数

#
# # '2.778'


# def average(array):
#     avg = [1, 2, 3, 4, 5, 4, 3, 2, 1]
#     n = len(array)
#     for num in array:
#         avg += 1.0 * num / n
#     return avg
# print (average())
