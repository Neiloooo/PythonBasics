# coding=utf-8
# 多态
class Dog(object):
    # 传入name属性
    def __init__(self, name):
        self.name = name

    def game(self):
        print ("%s正常的狗仔玩" % self.name)


class XiaoTianDog(Dog):
    def game(self):
        # 这里直接使用父类的name属性对子类进行赋值
        print ("%s哮天犬上天玩" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    # 这里传入父类对象,调用父类的属性
    # 这样所有其子类都可以传入,而且当我们调用子类的时候,实际调用的是子类重写的方法
    def game_with_dog(self, dog):
        print ("%s和%s快乐的玩耍" % (self.name, dog.name))


# 1.创建狗对象
# Python中不需要父类引用指向子类对象,右面写谁就会掉用哪个子类的方法和属性
wangcai = XiaoTianDog("飞天狗")
# 2.创建小明对象
xiaoming = Person("小明")
# 3.让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)
