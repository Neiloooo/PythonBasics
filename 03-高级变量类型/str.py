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

# 四,文本对齐
# 假设:以下内容从网络抓取,
# 要求:按照荀淑把他们居中对齐输出以下内容:
poem = [
    "登黄鹤楼",
    "王维",
    "白日衣裳尽",
    "黄河入海流"
]
for poem_str in poem:
    # 居中
    print ("|%s|" % poem_str.center(10))
    # ljust(10,"")左对齐
# 4.1去除空白字符
poem = [
    "\t\n登黄鹤楼",
    "王维",
    "白日衣裳尽\t\n",
    "黄河入海流"
]
for poem_str in poem:
    # 去除空白字符,然后居中居中
    print ("|%s|" % poem_str.strip().center(10))

# 4.2拆分和连接(类似java的stringbuffer)
# 要求:
# 1.将字符串的空白字符全部去掉
# 2.在使用""作为分隔符,拼接成一个整齐的字符串
poem_str = "登黄鹤楼\t王之涣\t\n白日依山尽"
print (poem_str)
# 1.拆分字符串,并且存入列表中,分割条件为空格
poem_list = poem_str.split()
print (poem_list)
# 2.合并列表中的字符串,使用空格作为分隔符,返回一个完整的字符串
result = " ".join(poem_list)
print (result)

# 五.字符串的切片,开始索引和结束索引中间的内容,(且不包含结束索引的内容)
# 第三个参数步长,每几个字符一组被分割开,倒序索引,最后一个字符是-1
# 通过切片获取字符串的逆序
num_str = "1234567"
# 开始索引-1,结束索引不指定,步长-1
str1 = num_str[-1::-1]
print str1
