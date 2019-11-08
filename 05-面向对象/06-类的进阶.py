# coding=utf-8
class Chinese:
    """"这是中国人的类"""
    pass


print (Chinese)

# 实例化一个类,创建一个类的对象
p1 = Chinese()  # 实例化
print (p1)


# 新式类(所有类如果没有父类最好都继承object类)
class Chinese(object):
    """"这是中国人的类"""
    government = "共产党"  # 数据属性

    def yi_er_san():
        print ("你好啊一二三")

    # 有参构造(java的)
    def cha_dui(self):
        print ("插队在前面")


# 类名.属性调用内部定义属性(与字典的调用方式相同)
print (Chinese.government)
# 类名.__dict__查看类的属性字典(属性字典里定义着key,value属性)
# 而类的属性与方法,是以key,value字典的形式保存的,在底层
print (Chinese.__dict__)
print (Chinese.cha_dui("你好老师"))
print (Chinese.yi_er_san())

# 属性:
# 数据属性,函数属性
