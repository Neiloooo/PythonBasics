# coding=utf-8
# Process类
# name 进程名
# args/kwgs:要传入的参数
# is_alive,判断进程是否存在
# run方法,start时候会默认调用重写的run方法


# 1.进程通信:进程队列Queue通信
import multiprocessing

# ①获取进程队列(记得与线程队列的区别)
# 队列的父子进程的传递类似于复制,父进程复制给子进程
# 子进程与主进程交互用进程队列
Q = multiprocessing.Queue
# 且args可以传入多个参数
p = multiprocessing.Process(target="类名", args=("参数这里是之前创建好的进程队列", Q,))
# 开启刚刚由继承获取的子进程
p.start()

# 2.进程通信:pipe管道,双向管道
parent_conn, child_conn = multiprocessing.Pipe()
# ②需要将子双向管道传递给子进程
p = multiprocessing.Process(target="类名", args=(child_conn,))
p.start()

# 3.Managers方式实现进程通信(进程间共享)
# Queue和pipe只是实现了数据交互,并没有实现数据共享,即一个进程去更改另一个进程的数据
