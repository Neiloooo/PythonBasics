# coding=utf-8
# 元组用()定义,且元组内的数据不能修改,只能取
# 元组主要保存不同类型的数据,而且是只读的tuple
# 元组的应用场景:
# 1.函数的参数与返回值(接受与返回多个数据)
# 2.格式字符串(格式化多个字符串的时候,本质上就是元组)
# 3.让列表不可被修改(保护数据安全)
info_tuple = ("zhangsan", 18, 175)
# 1.取值和取索引
print (info_tuple[0])
print (info_tuple.index("zhangsan"))

# 2.统计计数
print (info_tuple.count("zhangsan"))
# 统计元组中包含元素的个数
print (len(info_tuple))

# 3.循环遍历for循环能遍历所有非数字型数据
for my_info in info_tuple:
    # 使用格式字符串my_info这个变量不方便
    # 因为元组中通常保存的类型是不同的
    print (my_info)

# 4.元组和列表之间的相互转换
# tuple与list相互转换
