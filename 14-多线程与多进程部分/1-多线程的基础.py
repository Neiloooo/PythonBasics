# coding=utf-8
# 进程存在的意义: 内存地址相互独立,切换消耗时间与资源太大(最小资源单位)
# 线程: 在进程中,公用一套资源,快,便捷,但是不安全(最小的执行单元)
# ===========创建线程的方式===============
import threading


def dayin():
    # 子线程的打印
    print ("ok,子线程的调用")


t1 = threading.Thread(target=dayin())
t1.start()
# 主线程的打印
print ("ending,主线程没了")


# +++++++++++++++++++继承方式创建多线程+++++++++
# 创建一个类继承threading.Thead,默认重写run方法从而实现多线程
class MyThread(threading.Thread):
    def run(self):
        print (u"继承方式创建子线程成功了")


# 每次调用继承多线程的方法都会执行其中重写的run方法
t1 = MyThread()
t1.start()
print ("ending,主线程执行结束了")
