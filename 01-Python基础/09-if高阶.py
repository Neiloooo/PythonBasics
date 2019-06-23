# coding=utf-8
# elif相当于switch,case,希望判断多个条件,并且条件不同希望执行代码也不同的时候
# 使用elif,且都不满足的使用可以使用else收尾,相当于default()

# elif的练习一:
holiday_name = "平安夜"
# 如果是情人节,应该买玫瑰/看电影
if holiday_name == "情人节":
    print ("买玫瑰")
    print ("看电影")
# 如果是平安夜,应该吃苹果
elif holiday_name == "平安夜":
    print ("买苹果")
else:
    print ("别问,问就是996福报")

# if嵌套练习一:(和java的if,else一样),而双重门槛,主要通过格式来确定
has_ticket = True
knife_length = 15
if has_ticket:
    print ("车票检查通过,准备开始安检")
    if knife_length > 20:
        print ("您携带的刀太长了,有%d公分长,赶紧下车" % knife_length)
    else:
        print ("安检已经通过,抓紧上路")
else:
    print ("没票也想上车?")
