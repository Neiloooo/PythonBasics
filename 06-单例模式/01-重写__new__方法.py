# coding=utf-8
# _new_方法的重写
class MusicPlayer(object):
    # 重写object类的new方法
    def __new__(cls, *args, **kwargs):
        # 1.创建对象时,new方法会被自动调用
        print ("创建对象,分配空间")
        # 2.为对象分配空间,调用父类的new方法,并记录结果
        # 重写方法很固定,new方法是静态方法
        instance = super(MusicPlayer, cls).__new__(cls)
        # 3.返回对象的引用
        return instance

    def __init__(self):
        print ("播放器初始化")


# 创建播放器对象
player = MusicPlayer()
print (player)
