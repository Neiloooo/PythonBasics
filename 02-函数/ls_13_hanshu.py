# coding=utf-8
# 函数(方法?)
from __future__ import print_function


# 自定义函数
def multiple_table():
    # 如果不希望print换行,需要在器后面增加(, end="")
    row1 = 1
    while row1 <= 5:
        col = 1
        while col <= row1:
            # 单个*不再换行,2.7end函数需要导包
            print("*", end="")
            col += 1
        # 一行*输出之后,添加换行
        print("第%d行" % row1)
        print("")
        row1 += 1
