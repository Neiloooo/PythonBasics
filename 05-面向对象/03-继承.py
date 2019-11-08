# coding=utf-8
# 子类拥有父类的全部方法和属性
# 和java一样先执行父类代码
class Animal:
    def eat(self):
        print ("吃__")

    def drink(self):
        print ("喝__")


class Dog(Animal):
    # Dog继承Animal,子类拥有父类的全部属性和方法
    # 子类的特有方法bark
    def bark(self):
        print ("汪汪叫")


# 创建一个对象-狗对象(狗类又因为继承了Anmmal类,所以拥有动物类的所有属性和方法)
wangcai = Dog()
wangcai.eat()
wangcai.bark()


# ______super在重写父类方法时调用父类的方法_________________________________________________________________________________
# 2.7的Python中父类必须继承object类,才能跑起来
class Animals(object):
    def eat(self):
        print ("吃__")

    def bark(self):
        print ("动物叫")


class Dog(Animals):
    def eat(self):
        # 1.针对子类特有的需求,编写代码
        print ("狗吃骨头__")
        # 2.使用super关键字调用父类中封装的方法
        super(Dog, self).eat()
        # 3.增强方法
        print ("########FSFF")


xiaogou = Dog()
xiaogou.bark()
xiaogou.eat()


# _________私有属性和方法________________________________________________________________-
# 子类无法直接调用父类的私有方法和属性
# 但是子类可以通过调用父类的公有方法进而调用里面的私有方法和属性
# __________python可以多继承_____________________________________________________-
class A:
    def test(self):
        print ("test方法")


class B:
    def demo(self):
        print ("demo方法")


class C(A, B):
    """"C类继承A和B,同时具有多个父类的属性和方法"""

    def demo2(self):
        print ("我是C的方法")


# c创建子类对象,子类多继承,可以调用双亲的所有方法
c = C()
c.test()
c.demo2()
c.demo()
