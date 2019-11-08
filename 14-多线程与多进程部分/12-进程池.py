# coding=utf-8
# 进程同步 不仅需要线程同步,进程同样需要同步
# 加锁就相当于串行了,和线程一样
# Lock()


# 进程池
# 　设置进程池的大小为５
# pool = Pool(5)
# for i in range(100):
#     pool.apply(func="方法名",args=(i,)) #同步接口
#     pool.apply_async() #异步接口
#     注意这里的回调函数是在子进程中调用的
#     pool.apply_async(func="多进程调用的方法名",arg=(参数,),callback=进程执行完回调的的函数名)
# 　pool.close() 关池子
#   pool.join() 在子进程完成前,主进程会一直处于阻塞状态

