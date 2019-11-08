# coding=utf-8
import time

# 1.时间戳(从1970年到现在时刻的秒数)(计算)
print (time.time())

# 2.结构化时间(默认传参time.time,相当于当前时间戳),传入其他时间戳也一样
# 获取当前年月日时分秒星期几,类似(java的Date函数)
# 可以具体的获取当前年月日时分秒等
# 当地时间
print (time.localtime())
t = time.localtime()
print (t.tm_year)
# 显示周几
print (t.tm_wday)
# --结构化时间--UTC世界标准时间
print (time.gmtime())
# --逆向结构化时间转换成时间戳
print (time.mktime(time.localtime()))
# -----------------------------------------------
# 常用的字符串时间(被格式化的时间1995-02-08):
# 1.将结构化时间转换成字符串时间
# 传入参数为想要的日期格式:年月日时分秒,1995-02-08-10 18:19:10
print (time.strftime("%Y-%m-%d %X", time.localtime()))
# 2.将字符串时间转换为结构化时间strptime
# 可以供我们调用的对象
print (time.strptime("2019:12:24:17:50:38", "%Y:%m:%d:%X"))
# -----------------------------------------------------
# 将结构化时间转换为固定的格式化时间(参数为结构化时间)
print (time.asctime())
# 时间戳转换为固定的格式化时间(参数为时间戳)
print (time.ctime())
