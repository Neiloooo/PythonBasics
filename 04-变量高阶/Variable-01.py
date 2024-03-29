# coding=utf-8
# 变量分可变与不可变类型:
# 一,不可变类型:(一旦定义其中内容不可修改,只能更换变量地址)
# 数字类型:int,bool,float,complex
# 字符串:str
# 元组:tuple

# 二,可变类型(定义后可以通过.方法,对其进行内容上的修改,但是如果=的话(相当于java的new))
# 列表:list
# 字典:dict

# 三.字典的修改与赋值(字典的地址是不变的)
# 使用方法修改其内容不会更改其地址,使用赋值语句就等于new
a = [1, 2, 3]
a.append(999)
a.remove(2)

# 字典类型的key只能是不可变类型的数据
# 即:数字,元组,字符串
# 初始化字典
d = {}
# 为字典添加数据
d["name"] = "xiaoming"
d[1] = "haha"
# 元组当key
d[(1,)] = "元组"
# 不能使用列表与字典作为键值对的key

# 哈希,提取数据的特征码(指纹)
# Python的哈希只能接收一个不可变类型的数据作为参数
# 并且返回一个整数

