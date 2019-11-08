# coding=utf-8
import re

a = [0XC1, 0X02, 0X55, 0X44, 0XFF, 0X90]
t = "0xc1 0x02 0x55 0x44 0xff 0x90"
res = list(filter(None, t.split(" ")))  # 此处必须加一个list，因为filter转化后要以list展示，否则报错error<filter object at 0x02C18A70>
print(res)
