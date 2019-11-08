# coding=utf-8
# 不同语言之间数据交换的桥梁

# # 1.读写文件,字典与字符串等数据类型的转换(字典转换为字符串)
# dic = '{"name": "alex"}'
# # 2.打开hello,文件没有则创建,权限设置为只写
# f = open("hello", "w")
# # 写入元组
# f.write(dic)
#
# # 读取文件中的数据
# f_read = open("hello", "r")
# data = f_read.read()
# print (type(data))
# # 将字符串转换为其原本的数据类型
# data = eval(data)
# print (data["name"])
# _________json任何语言之间都可以传送数据__________________
import json

# 自定义字典
# dic = {"name": "alex"}
# # 任意类型数据转换成json字符串类型
# data = json.dumps(dic)
# 同样可以存入文件中
# f = open("new_hello", "w")
# f.write(data)
f_read = open("new_hello", "r")
# 将json字符串转换为起原本的类型(这里是字典)
data = json.loads(f_read.read())
print (data)
print (type(data))