# coding=utf-8
# 自python2.6开始，新增了一种格式化字符串的函数str.format()，此函数可以快速处理各种字符串。
# 语法: 相当于对于字符串的格式化刷子
#   它通过{}和:来代替%。
#   请看下面的示例，基本上总结了format函数在python的中所有用法
# 通过位置
from __future__ import print_function

print('{0},{1}'.format('chuhao', 20))

print('{},{}'.format('chuhao', 20))

print('{1},{0},{1}'.format('chuhao', 20))

# 通过关键字参数
print('{name},{age}'.format(age=18, name='chuhao'))


# 通过类映射
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'This guy is {self.name},is {self.age} old'.format(self=self)


print(str(Person('chuhao', 18)))

# 通过列表list映射
a_list = ['chuhao', 20, 'china']
print('my name is {0[0]},from {0[2]},age is {0[1]}'.format(a_list))
# my name is chuhao,from china,age is 20

# 通过映射 dict
b_dict = {'name': 'chuhao', 'age': 20, 'province': 'shanxi'}
print('my name is {name}, age is {age},from {province}'.format(**b_dict))
# my name is chuhao, age is 20,from shanxi

# 填充与对齐
print('{:>8}'.format('189'))
#     189
print('{:0>8}'.format('189'))  # 前置位补齐八位,没有的补0
# 00000189
print('{:a>8}'.format('189'))  # 前置位补齐8位,没有的补a
# aaaaa189

# 精度与类型f
# 保留两位小数
print('{:.2f}'.format(321.33345))
# 321.33

# 用来做金额的千位分隔符
print('{:,}'.format(1234567890))
# 1,234,567,890

# 其他类型 主要就是进制了，b、d、o、x分别是二进制、十进制、八进制、十六进制。
# 对format里的数字进行不同进制的格式化
print('{:b}'.format(18))  # 二进制 10010
print('{:d}'.format(18))  # 十进制 18
print('{:o}'.format(18))  # 八进制 22
print('{:x}'.format(18))  # 十六进制12

grade_list = [0x03, 0x02, 0x01, 0x00]
level_list = [0x0e, 0x0d, 0x0c, 0x0b, 0x0a, 0x09, 0x08, 0x07, 0x06, 0x05, 0x04, 0x03, 0x02, 0x01]
for grade in grade_list:
    for level in level_list:
        print("x{0:02X} 0x{1:02X}".format(grade, level))
        # x03 0x0E
