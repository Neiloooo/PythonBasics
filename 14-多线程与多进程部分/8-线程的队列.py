# coding=utf-8
# 队列(重要)(线程安全的数据结构)
# 线程安全
# 多线程专用数据结构
# 列表线程不安全

import Queue  # 引入线程队列

# 设置五个数据
q = Queue.Queue(5)  # 默认模式:先进先出
q.put(12)
q.put("hello")
q.put({"name": "aa"})

# 模式:先进后出

# 设置为后进先出模式
Q = Queue.LifoQueue
# 返回列队的长度
Q.qsize()
# 实际上意味着等到列队为空,再执行别的操作
Q.join()
