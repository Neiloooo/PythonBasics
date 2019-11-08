# coding=utf-8
# 小明小美(两个对象由同一个类产出,但是对象各自独立)
# 小明,小美爱跑步案例中,小明与小美对象之间的属性互相独立,
# 且互相不干扰(内存中创建的对象空间互相不干扰)

# 在房子里摆放家具(一个对象套一个对象(房子对象里包含家具))
# 家具类
class HouseItem:
    def __init__(self, name, area):
        # 定义家具类的两个属性
        self.name = name
        self.area = area

    def __str__(self):
        # 重写str属性,定义变量输出变量名返回字符串,而不是组织
        return "[%s]占地%.2f" % (self.name, self.area)


# 房子类
class House:
    # 初始化方法里定义属性
    # 且,只有需要从外部传递的参数才需要在初始化方法中定义形参
    def __init__(self, house_type, area):
        # 通过形参传入House对象的房子类型属性与占地面积属性
        self.house_type = house_type
        self.area = area
        # 定义剩余面积的对象属性
        self.free_area = area
        # 家具名称列表(房子对象中有哪几个家具对象)(使用列表,数组接收)
        self.item_list = []

    # 重写类的str方法,用来直接输出自定义(字符串)
    def __str__(self):
        # Python能够自动的将一对括号内部的代码连接在一起
        return "户型:%s\n总面积:%.2f[剩余:%.2f]\n家具:%s" \
               % (self.house_type, self.area,
                  self.free_area, self.item_list)

    # 自定义方法,添加家具的方法
    def add_item(self, item):
        # 添加家具的方法3个需求:
        # 1.判断家具的面积是否超过剩余面积,如果超过不能添加这件家具
        if item.area > self.free_area:
            print ("%s的面积太大了,无法添加" % item.name)
            return
        # 2.将家具的名称追加到家具名称列表中
        self.item_list.append(item.name)
        # 3.用房子的剩余面积-家具面积=房子添加家具后的剩余面积,为房子对象的剩余面积赋值
        self.free_area = self.free_area - item.area
        print ("要添加%s" % item)


# 1.创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
print (bed)
print (chest)

# 2.创建房子的对象
# 相当于java的new对象
my_home = House("两室一厅", 60)
# 调用House对象的自定义方法进行添加家具
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print (my_home)


# -----------------------------------------------------------------------
# 士兵开枪,ak47突突突
# 枪类
class Gun:
    # 通过初始方法,设置对象的属性(类似于java的有参构造,可以直接传入实参对对象进行赋值)
    def __init__(self, model):
        # 1.枪的型号(设置枪的类型由形参传递进来)
        self.model = model
        # 子弹的数量(设置子弹数量的默认初始值为0)
        self.bullet_count = 0

    # 自定义增加子弹的方法
    def add_bullet(self, count):
        self.bullet_count += count

    # 自定义射击的方法
    def shoot(self):
        # 1.判断是否还有子弹数量
        if self.bullet_count <= 0:
            print ("[%s]没有子弹了.." % self.model)
            # 没有子弹直接返回,不再向下执行
            return
            # 2.发射子弹,-1
        self.bullet_count = self.bullet_count - 1
        # 3.提示发射信息
        print ("[%s]突突突,,还剩[%d]发子弹" % (self.model, self.bullet_count))


# 1.创建枪对象
ak47 = Gun("AK47")
ak47.add_bullet(10)
ak47.shoot()


# 如果不直到对象的属性具体设置什么初始值,可以为其设置为None进行占位
class Soldier:
    def __init__(self, name):
        # 1.定义姓名属性为调用函数时需要通过实参赋值
        self.name = name
        # 2.枪-且新兵没有枪(这里不知道枪该如何设置初始值,所以先用None进行占位)
        # 这里的None相当于万能类型的占位符
        # 而且这里要引用类的对象必须是去驼峰形式,Python才会认你是哪个类的对象
        # 但是这个对象如果想要从其他类获得引用类型的对象的话,就需要定义None占位符,等到以后我们为其赋值
        self.gun = None

    # 自定义开火方法:
    def fire(self):
        # 1.判断士兵对象的枪属性是否为None
        if self.gun is None:
            print ("[%s]还没有枪.." % self.name)
            # 没有枪就返回
            return
        # 2.高喊口号
        print ("冲啊...[%s]" % self.name)
        # 3.让枪装子弹,add_bullet,表示调用Gun类的方法
        self.gun.add_bullet(50)
        # 4.让枪发射子弹
        self.gun.shoot()


xusanduo = Soldier("许三多")
# 3.将已经枪对象存入许三多对象的枪属性里
# 类似于java的set属性,但是java里有严格的类型要求
# 要求对象属性的类型与传入的对象类型必须一致
xusanduo.gun = ak47
print (xusanduo.gun)


# ++++++++++++is与==+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 身份运算符:
# is,比较内存地址(两个变量的引用对象),判断引用的是否为同一个对象
# is,用来判断内存地址,==判断值
# 建议对于none的判断来说,使用is进行判断
# +++++++++++++++私有属性与私有方法++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++===
# 1.私有属性:不希望对外界公开的属性
# 2.私有方法:不希望对外界公开的方法
# 1.在定义属性或方法时,在属性名或者方法名前增加两个下划线__,就是私有属性和方法
class Women:
    def __init__(self, name):
        self.name = name
        self.age = 18

    def secret(self):
        print ("%s的年龄是%d" % (self.name, self.age))
