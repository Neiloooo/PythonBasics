# coding=utf-8
# 1.类是图纸,对象是实物
# 2.同一个类,属性可能不同
# 3.类名要满足大驼峰命名法:CapWords
# 4.对象的特征描述:属性,对象的具体行为:方法

# 一.dir内置对象
# 可以通过dir查看对象的所有方法和属性
# __方法名__是Python针对对象提供的内置方法名
# ----------------------------------------------------
# 类与方法
# 小猫爱吃鱼,小猫爱喝水
class Cat:
    def eat(self):
        print ("小猫爱吃鱼")

    def drink(self):
        print ("小猫爱喝水")


# 创建猫对象(Python里=号相当于new对象)
# 等号左侧是对象引用,右侧是对象
# 直接打印对象可以看出对象的地址与对象是由哪个类创建的
tom = Cat()

# 可以使用 .属性名,利用赋值语句为其添加属性名
# 这样可以不修改类,进而对对象进行属性修改(不推荐)
tom.name = "TOM"

# 对象调方法
tom.eat()
tom.drink()


# --------------------------------------------------------------------------------
# 类中的self属性(有点类似java的this)
# 哪一个对象调用的方法,self就是哪个对象
class Cat:
    def eat(self):
        # 我们可以通过self指代(new)的对象引用,谁调用我,我就是self
        # 具体使用可以在类的方法内调用对象的属性或方法
        # 总体来讲:指代(new)出来的对象的引用
        print ("%s爱吃鱼" % self.name)

    def drink(self):
        print ("小猫爱喝水")


# 创建猫对象
tom = Cat()
tom.name = "TOM"
tom.eat()


# ---------------------------------------------------------------------
# 初始化方法
# 类名创建对象的时候:1.分配空间2.为属性初始化
# _init_方法是专门用来定义一个类具体有哪些属性的方法
class Cat:
    def __init__(self):
        print ("创建对象的时候会自动调用这个初始化方法")
        # self.属性名=属性的初始值
        # 为类定义初始化name属性
        self.name = "TOM"


# 使用类名()创建对象的时候,会自动调用初始化方法_init_
tom = Cat()
# 输出对象的初始化属性
print (tom.name)


# =================================================================
# 利用参数设置属性初始值:
class Cat:
    def __init__(self, new_name):
        print ("这是一个初始化的方法")
        # self.属性名=属性的初始值
        # self.name="Tom"
        # 设置New的Cat对象的name属性为传入的new_name形参的值
        self.name = new_name

    def eat(self):
        print ("%s爱吃鱼" % self.name)


# 使用类名()创建对象的时候,会自动调用初始化方法_init_
# 我们在初始化的方法里是设置了对象name的属性为传参的new_name
# 相当于java的setName
# 相当于java的有参构造(直接传参就可以达到对对象赋值的目的)
tom = Cat("张三")
print(tom.name)
tom.eat()


# ------------------------------------------------------------------------
# _del_方法(当一个对象从内存中销毁前,会自动调用_del_方法)
class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print ("%s来了" % self.name)

    def __del__(self):
        print ("%s 我去了" % self.name)


tom = Cat("Tom")
print (tom.name)
# del关键可以删除一个对象
del tom
print ("_" * 50)


# --------------------------------------------------------------
# 对象的生命周期,一个对象从调用类名创建,生命周期开始
# 一个对象的_del_方法一旦被调用,生命周期结束
# 在对象的生命周期内,可以访问对象属性,或者让对象调用方法
# 对象开始调用_init方法初始化,从内存中被消除的时候会调用_del_方法
# 如果想在对象对象被销毁前统一执行一些事情,可以重写_del_方法
# _______________________________________________________________________________________
# _str_方法,(必须返回一个字符串)
# 有点类似(重写toString方法)
class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print ("%s来了" % self.name)

    def __del__(self):
        print ("%s 我去了" % self.name)

    # 如果希望print(对象变量),输出的是自定义内容,可以重写__str__fangfa1
    def __str__(self):
        # 重写__str__方法必须返回给字符串
        return "我是小猫[%s]" % self.name


tom = Cat("Tom")
print (tom.name)
# 重写_str_方法可以直接通过查看name的值,而不需要再调用.name
# 类似java的重写toString方法
print (tom)
# del关键可以删除一个对象
del tom
print ("_" * 50)
