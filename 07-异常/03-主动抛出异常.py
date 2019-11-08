# coding=utf-8
# 案例,如果输入密码位数小于8,主动抛出异常
# 这里的函数只有逻辑判断,如果用户输入密码大于8,就正常执行(返回用户输入的密码)
# 如果密码小于8,则创建异常
def input_password():
    # 1.提示用户输入密码
    pwd = input("请输入密码:")
    # 2.判断密码长度>=8,返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    # 3.如果<8主动抛出异常
    print ("主动抛出异常")
    # 1>创建异常对象-可以使用错误信息字符串作为参数
    ex = Exception("密码长度不够")
    # 2.主动抛出异常
    raise ex


# 提示用户输入密码:(捕获异常)
try:
    print (input_password())
except Exception as result:
    print (result)
