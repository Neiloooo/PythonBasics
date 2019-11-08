# coding=utf-8
# 我们可以完成大部分工作。但当Python需要通过网络与其他的平台进行交互的时候，必须考虑到将这些数据类型与其他平台或语言之间的类型进行互相转换问题。打个比方：
# C + +写的客户端发送一个int型(4字节)变量的数据到Python写的服务器，Python接收到表示这个整数的4个字节数据，怎么解析成Python认识的整数呢？
# Python的标准模块struct就用来解决这个问题。struct模块的内容不多，也不是太难，下面对其中最常用的方法进行介绍：
#
# 1、 struct.pack:(字节流转换为字符串)
# struct.pack用于将Python的值根据格式符，转换为字符串（因为Python中没有字节(Byte)类型，可以把这里的字符串理解为字节流，或字节数组）。
# 其函数原型为：struct.pack(fmt, v1, v2, ...)，参数fmt是格式字符串，关于格式字符串的相关信息在下面有所介绍。v1, v2, ...
# 表示要转换的python值。
#
# 2、 struct.unpack:(字符串转换为字节流)
# struct.unpack做的工作刚好与struct.pack相反，用于将字节流转换成python数据类型。它的函数原型为：struct.unpack(fmt, string)，该函数返回一个元组。

from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
import struct

a = 20
b = 400
s = struct.pack('ii', a, b)  # 转换为字节流
print(s, type(s))
# 输出：b'\x14\x00\x00\x00\x90\x01\x00\x00' <class 'bytes'>
print('length: ', len(s))
# 输出：length:  8
s2 = struct.unpack('ii', s)  # 字节流转换为正常的
print(s2)
# 输出：(20, 400)

s2 = struct.unpack('ii', s)
# 报错：unpack requires a buffer of 4 bytes
# ==>解压需要一个4字节的缓冲区，也就是说'ii'表示8个字节的缓冲

##格式符"i"表示转换为int，'ii'表示有两个int变量。
# 进行转换后的结果长度为8个字节（int类型占用4个字节，两个int为8个字节）
# 可以使用python的内置函数repr来获取可识别的字符串，其中十六进制的0x00000014, 0x00001009分别表示20和400。


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import binascii

values = (1, 'abc', 2.7)
# 一个字符代表四个字节
s = struct.Struct('I3sf')
packed_data = s.pack(*values)
unpacked_data = s.unpack(packed_data)
print("+++++++++++++++++++++++")
print('Original values:', values)
print('Format string :', s.format)
# 所以这里的尺寸是12个字节
print('Uses :', s.size, 'bytes')
# 按照ascii进行格式化
print('Packed Value :', binascii.hexlify(packed_data))
print('Unpacked Type :', type(unpacked_data), ' Value:', unpacked_data)
