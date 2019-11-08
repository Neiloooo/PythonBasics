# coding=utf-8
# 信号量
# 可以指定若干个线程同时处理数据
# 信号量也是同步的
# Semaphore,也是锁的一种
# 信号量也是锁的一种
import threading
# semaphore=threading.Semaphore 创建信号量锁
# semaphore.acquire() 需要信号量锁(加锁)
