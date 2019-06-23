# coding=utf-8
# 2.7版本要导包
from __future__ import print_function

# break:的使用,当该层循环遇到break就跳出该层循环,直接执行最终语句
i = 0
while i < 10:
    if i == 3:
        print("遇到三了溜了")
        break
    print(i)
    i += 1
print("结束了")

# continue: 当该层循环遇到continue,就不执行当前循环代码,但是后面的执行顺序仍然会继续
# break是遇到就向下完全没了,
# continue遇到也是跳出,但是是跳出当次,但是注意,当次i仍然是3,如果不进行=1
# 会死循环
i = 0
while i < 10:
    # continue某一条件满足是,不执行后续重复代码
    # i==3
    if i == 3:
        # 注意:在循环中,如果使用continue这个关键字
        # 在使用关键字之前,需要确认循环的计数是否修改
        # 否则可能会有导致死循环
        i += 1

        continue
    print(i)
    i += 1

# 循环嵌套
# 练习一:打印小星星,每一行的星号数量一次递增
row = 1
while row <= 5:
    print("*" * row)
    row += 1
# 默认情况下,print函数输出内容之后,会自动在内容末尾增加换行
# 如果不希望print换行,需要在器后面增加(, end="")
row1 = 1
while row1 <= 5:
    col = 1
    while col <= row1:
        # 单个*不再换行,2.7end函数需要导包
        print("*", end="")
        col += 1
    # 一行*输出之后,添加换行
    print("第%d行"%row1)
    print ("")
    row1 += 1
