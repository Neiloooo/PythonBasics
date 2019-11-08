# coding=utf-8
# import configparser
#
# # 引入模块实例化对象
# config = configparser.ConfigParser()  # config={}
# # ----------相当于增加方法,添加配置信息到某个文件中----------------------------------
# # 配置文件以键值对格式读取(然后将这个数据写入到自定义的配置文件中)
# config["DEFAULT"] = {
#     "ServerAliveInterval": "45",
#     "Compression": "yes"
# }
#
# # 写入上面的配置文件到目录下的example.ini文件中
# with open("example.ini", "w") as f:
#     config.write(f)
# ------------查询方法-----------------------------------------
import configparser

# 创建configer对象(读取example.ini文件)
config = configparser.ConfigParser()
config.read("example.ini")
print (config.sections())  # 获取配置文件中的文件名
print ("bitbucket.org" in config)  # 判断这名(块名)的配置是否在配置文件中
print (config["bitbucket.org"]["User"])  # 取出配置文件中User的值:hg
# 遍历配合文件中所有字典的键值,默认[DEFAULT]的也被遍历出来了
for key in config["bitbucket.org"]:
    print (key)
# 以列表形式遍历配置文件
print (config.options("bitbucket.org"))
