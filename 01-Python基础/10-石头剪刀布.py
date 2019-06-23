# coding=utf-8
# 导包,注意放在顶部
import random

# 请出拳,且1是石头,2是剪刀,3是布
player = int(input("请输入您要出的拳,1是石头,2是剪刀,3是布"))
# 随机数,random.randint制造范围内的随机数
computer = random.randint(1, 3)
print ("玩家选择的拳头是%d-电脑的出拳是%d" % (player, computer))
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print ("你赢了")
# 平局
elif player == computer:
    print ("平局")
# 其他情况都是电脑获胜
else:
    print ("白给少年,再来一次")
