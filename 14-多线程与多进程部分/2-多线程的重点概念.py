# coding=utf-8
# 多个线程对一个资源进行处理,会出现不安全(不同步)的问题
# 1.同步锁用来处理数据安全问题,
# 2.死锁,递归锁
# 3.队列
# 4.信号量和同步对象(了解就好)
# 5.进程

# 并发,指系统具有 处理多个任务 (动作)的能力(CPU切换完成并发)
# 并行:指系统具有 同时 处理任务的能力(多核cpu)

# 同步与异步:
# 同步: 当进程执行到一个IO(等待外部数据)的时候称,===等:同步
# 异步:                                   ,===不等,中间可以做其他的事情,等到数据接收成功,再再回来处理


