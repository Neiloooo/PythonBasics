# coding=utf-8
# 新式类(所有类如果没有父类最好都继承object类)
class Chinese(object):
    """"这是中国人的类"""
    government = "共产党"  # 数据属性

    # Python的初始化时在类中的,当调用类实例化的时候就会默认触发初始化函数
    # 使用__init__方法可以自动将调用者的参数传递给类
    # 而且会返回对象地址给p1
    # 1.定制对象的属性
    # 2.自定执行初始化方法
    # 3.必须传入self参数
    # 4.self就是调用的对象自己
    # 5.return self,Python自动返回字典(mingzi:name,nianling:age,xingbie:gender)
    def __init__(self, name, age, gender):
        print ("每次实例化对象都会触发init方法")
        # 这里的self就是我们实例化的对象p1
        # 这些属性相当于赋值给了p1
        self.mingzi = name  # 这里相当于p1.mingzi=name
        self.nianling = age  # p1.nianji=age
        self.xingbie = gender  # p1.xingbie=gender
        print ("实例化结束了")

    # 类中定义的函数都要求第一个参数定义为self,为了接受对象名自己
    # 这样我们就可以在方法中调用对象传入的参数
    def yi_er_san(self):
        print ("你好啊一二三")

    # 需要对象传参的(类似java的有参构造)
    def cha_dui(self):
        print ("%s插队在前面" % self.mingzi)


# 类的实例化(实例就是执行的__init__方法)
p1 = Chinese("袁浩", 18, "女生")
# 查看赋值后的对象字典
print (p1.__dict__)
# 通过字典的方式调用对象的属性
print (p1.__dict__["mingzi"])
# 调用对象的属性
print (p1.mingzi)
# 调用类的全局变量
p1.government
# 调用实例对象的方法(Python会自动把自己当做参数传入到方法当中)
# 且实例只有数据属性,没有函数属性
p1.cha_dui()
