# coding=utf-8
# 多进程:主要解决GIL锁问题(一般用的少,因为消耗太大效率较低)
# 调用方法和多线程基本一致(实例,开启,)与继承
# 进程的pid,os.getpid()
# 进程的ppid,os.getppid(),父进程的pid
