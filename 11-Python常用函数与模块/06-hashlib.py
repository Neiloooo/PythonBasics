# coding=utf-8
import hashlib

# 创建hashlib加密方式
obj = hashlib.md5()
# 调用update方法进行加密(要加密的数据,变成字节类型默认的编码方式)
obj.update("hello".encode("utf-8"))

print (obj.hexdigest())
