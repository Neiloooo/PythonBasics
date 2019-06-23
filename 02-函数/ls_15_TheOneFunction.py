# coding=utf-8
# 定义的函数需要被调用,不会主动执行
# 类似于java类的全局变量
name = "小明"


# def是告诉Python解释器知道下方定义一个函数:
def say_hello():
    """"
    函数的注释
    """
    print ("hello1")


print (name)
# 如果是调用当前模块的模块的函数,直接使用函数名即可
# 在函数上使用ctrl+Q,来查看其注释
say_hello()
print (name)
