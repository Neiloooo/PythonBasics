# coding=utf-8
# elif相当于switch,case,希望判断多个条件,并且条件不同希望执行代码也不同的时候
# 使用elif,且都不满足的使用可以使用else收尾,相当于default()

# elif的联系一:
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
