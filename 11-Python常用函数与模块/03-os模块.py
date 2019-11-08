# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import os

print (os.getcwd())
# 改变当前工作目录
os.chdir("目录名")
# 增加文件夹
os.makedirs()
# 删除文件夹
os.removedirs()
# 删除文件
os.remove()
# 当前目录的文件
os.listdir()
# 获取文件属性
os.stat()
# 切割文件路径(将文件名与文件路径分割,通过绝对路径)
os.path.split()

# 重要:join
# 将两个路径拼接(绝对与相对路径的结合与转换)
a = "文件所在目录"
b = "相对路径"
os.path.join(a, b)
