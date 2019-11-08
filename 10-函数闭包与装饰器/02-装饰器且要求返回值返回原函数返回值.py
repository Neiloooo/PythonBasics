# coding=utf-8
# 装饰器的架子
import time


# timmer的功能是计算函数运行时间
def timmer(func):
    def wrapper():
        print (func)
        # 记录函数开始时的时间
        start_time = time.time()
        # 这里将函数返回值封装给res就可以得到原函数的返回值
        res = func()  # 在这里对传入函数加强就行了
        # 记录函数结束时的时间
        stop_time = time.time()
        print ("运行时间是%s" % (stop_time - start_time))
        #这里就可以直接返回原函数的返回值
        return res

    # timmer函数运行返回wrapper函数
    return wrapper


@timmer  # 相当于test=timmer(test)
def test():
    # 让函数过3秒再运行
    time.sleep(3)
    print ("test函数运行完毕")


# test = timmer(test)
# test()
# 等价于@timer就相当于test=timmer(test)

# 这样就真正的实现了不改变源码与调用方式的情况下对test()函数进行增强
# 但是这样在返回值上有问题,因为本质上调用的是wrapper函数,所以返回的是wrapper函数里的返回值
# 而我们想要的返回值是test里的,所以需要在增强函数里将原函数的返回值返回
test()
