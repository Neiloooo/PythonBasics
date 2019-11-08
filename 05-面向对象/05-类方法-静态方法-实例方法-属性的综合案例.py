# coding=utf-8
# 游戏设计的综合案例
class Game(object):
    # 类属性,应该再类里定义
    top_score = 0

    def __init__(self, player_name):
        # 实例属性再init方法内定义
        self.player_name = player_name

    # 因为帮助信息不需要类属性与实例属性,所以可以定义成静态方法
    @staticmethod
    def show_help():
        print ("帮助信息:让僵尸进入大门")

    # 定义类方法,因为需要类属性top_score
    @classmethod
    def show_top_score(cls):
        # 类方法中,只需要cls.属性名就可以定义类属性
        print ("历史记录%d" % cls.top_score)

    # 定义实例方法,因为要用到实例传递进来的形参
    def start_game(self):
        print ("%s开始游戏啦..." % self.player_name)


# 1.查看游戏的帮助信息
Game.show_help()
# 2.查看历史的最高分
# 调用类方法也不需要传递属性,因为类属性在类的内部
Game.show_top_score()
# 3.创建游戏对象
game = Game("小明")
