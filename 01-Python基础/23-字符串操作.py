# -*- coding:utf-8 -*-


# import time
#
# # 获得当前时间时间戳
# now = int(time.time())
# # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
# timeStruct = time.localtime(now)
# strTime = time.strftime("%Y-%m-%d-%H:%M", timeStruct)
#
# print(strTime)
# sheet_name_xls = (u'测试专用表格 %s' % strTime)
# print(sheet_name_xls)


# 格式化字符串
# 槽号绑定信号的函数
def soltToSingnal(solt):
    # 槽号与信号绑定,1,2,3,4,5,6 与信号Y1,Y2,Y3,Y4,Y5,Y6
    solt = "Y" + str(int(solt))
    print (solt)


soltToSingnal(1)
