# -*- coding:utf-8 -*-
from __future__ import print_function
import time


fmt='%Y-%m-%d %a %H:%M:%S'      #定义时间显示格式
Date=time.strftime(fmt,time.localtime(time.time()))     #把传入的元组按照格式，输出字符串
print('获取当前的时间：', Date)