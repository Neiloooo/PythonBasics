# coding=utf-8
# 16进制转换成10进制
buf=['0x55', '0xaa', '0x1', '0x0', '0xa', '0x60', '0x1', '0x1', '0x54', '0x65', '0x73', '0x74', '0x55', '0x61', '0x72', '0x74']
list1 = []
for i in buf:
    i = int(i, 16)
    list1.append(i)
print list1