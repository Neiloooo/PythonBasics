# coding=utf-8
# 实现单例模式的案例:
# 由非单例模式,进行重写new方法实现单例模式
class MusicPlayer(object):
    # 记录第一个被创建的对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否为空对象
        if cls.instance is None:
            # 2.调用父类的方法为第一个对象分配空间
            cls.instance = super(MusicPlayer, cls).__new__(cls)

        # 3.返回类属性保存的对象引用,这样每次创建对象的时候都是同一个内存地址
        #也就是相同的对象
        return cls.instance


# 创建多个对象
player1 = MusicPlayer()
print (player1)
player2=MusicPlayer()
print (player2)
