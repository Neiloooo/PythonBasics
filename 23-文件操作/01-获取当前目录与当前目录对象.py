#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os, sys

FileName = os.getcwdu()
frequency2 = unicode(FileName).encode('utf-8')
Filename2 = frequency2 + "\\"
str = "E:/PythonWork/Demo/23-文件操作/01-获取当前目录与当前目录对象.py"
# 打印当前目录
# 获取 "."之前的字符(包含点) 结果.python

print(str.split('/')[-1])
# print "当前工作目录 : %s" % frequency2 + "\\"
# # 打开 "/tmp"
# fd = os.open( "/tmp", os.O_RDONLY )

# # 打印当前目录
# print "当前工作目录 : %s" % os.getcwdu()

