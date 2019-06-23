# coding=utf-8
# 字符串,有索引概念,从0开始,可以看成一个字符组成的数组
Str1 = "hello python"
print (Str1[6])

# for循环出字符串中的所有字符
for char in Str1:
    print (char)

# 1.统计字符串长度
print (len(Str1))
# 2.统计某一个小(子)字符串出现的次数
print (Str1.count("llo"))
# 3.某一个子字符串出现的位置
print (Str1.index("llo"))

# 二.字符串的常用方法
# \t,横向指标符号
# ①判断空白字符
space_str = ""
# 判断字符串是否只包含空白字符,如果是则返回True
print (space_str.isspace())
# 2.判断字符串中是否只包含数字,且不能包含小数
num_str = "1"
# 数字,(1),转义的"\u00b2"
print (num_str.isdigit())

# 三,字符串的查找和替换
hello_str = "hello world"
# ①判断是否以指定字符串开始
print (hello_str.startswith("hello"))
# ②判断是否以指定字符串结束
print (hello_str.endswith("world"))
# ③.查找指定字符串
# index同样可以查找指定的字符串在大字符串中的索引
print (hello_str.find("llo"))
# index如果指定的字符串不存在会报错
# find方法如果指定的字符串不存在,会返回-1
print (hello_str.find("adb"))
# ④替换字符串,replace方法执行完成后,会返回一个新的字符串,不会修改原有字符串
print (hello_str.replace("world", "python"))
