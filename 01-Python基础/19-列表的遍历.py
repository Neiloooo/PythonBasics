# coding=utf-8

# 定义唤醒频率列表1
FREQuencyList1 = [6000000000, 5900000000, 5840000000, 5830000000, 5800000000, 5700000000, 5700000000]
# 定义唤醒频率列表2(0.1到5.6)
FREQuencyList2 = range(100000000, 5600000000, 100000000)
# for i in FREQuencyList2[::-1]:
#     print i
#     FREQuencyList1 = FREQuencyList1.append(i)
# print FREQuencyList1
A=FREQuencyList1+FREQuencyList2[::-1]
print A