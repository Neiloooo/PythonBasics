# -*- coding: utf-8 -*-
from __future__ import print_function
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# 定义全局变量存储登录状态
user_dic = {'uername': None, 'login': False}


# 定义有参数的装饰器
def auth(type="AABB"):
    def auth_func(func):
        def wrapper(*args, **kwargs):
            # 添加判断,如果已经登录过了不需要再登录
            if user_dic['username'] and user_dic['login']:
                res = func(*args, **kwargs)
                return res

            # 为原函数增强(验证用户名与密码进行权限认证)
            username = input('用户名: ').strip()
            passwd = input('密码: ').strip()
            if username == 'ss' and passwd == '123':
                # 如果没登录,则进行登录,并且将将全局变量修改为已登录状态
                # 以便于下次验证该用户是否登录
                user_dic['username'] = username
                user_dic['login'] = True

                # 为被增强的函数增加返回值与参数
                res = func(*args, **kwargs)
                # 返回返回值
                return res
            else:
                print('用户名或密码错误')

        return wrapper

    return auth_func


@auth(type="AABB")
def index():
    print("欢迎来到主页")


@auth(type="AABB")
def home(name):
    print("%s欢迎回家" % name)


index()
home('ss')
