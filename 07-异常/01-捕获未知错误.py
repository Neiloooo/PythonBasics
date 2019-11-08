# coding=utf-8
# 捕获未知异常(Exception)
try:
    num = int(input("请输入一个整数:"))
    result = 8 / num
    print (result)
except Exception as result:
    print ("未知错误%s" % result)
