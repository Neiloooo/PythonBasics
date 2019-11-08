# coding=utf-8
# 实现单例模式的案例:
# 由非单例模式,进行重写new方法实现单例模式
class MusicPlayer(object):
    # 记录第一个被创建的对象的引用
    instance = None

    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否为空对象
        if cls.instance is None:
            # 2.调用父类的方法为第一个对象分配空间
            cls.instance = super(MusicPlayer, cls).__new__(cls)

        # 3.返回类属性保存的对象引用,这样每次创建对象的时候都是同一个内存地址
        # 也就是相同的对象
        return cls.instance

    def __init__(self):
        # 1.判断是否执行过初始化动作,如果执行过就结束初始化
        if MusicPlayer.init_flag:
            return
        # 2.如果没有执行过,在执行初始化动作
        print ("初始化播放器")
        # 3.修改类属性的标记,当执行到这步的时候,就需要修改初始化标记,告诉已经初始化过了
        MusicPlayer.init_flag = True

        # 创建多个对象


player1 = MusicPlayer()
print (player1)
player2 = MusicPlayer()
print (player2)
