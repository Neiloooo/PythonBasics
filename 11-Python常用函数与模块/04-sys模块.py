# coding=utf-8
# sys模块
import sys
import time

# # 退出程序,正常退出时exit(0)
# sys.exit(0)
# # 获取解释器的版本:
# sys.version
# # 获取操作系统平台的名称
# sys.platform

# 使用sys模块打印进度条
for i in range(10):
    # print也是通过这句话出来的,
    # 向屏幕响应相应内容
    # stdout是放入缓存区里等打印输出完一次性显示出来
    # 百分比思路:以执行字节/总的字节%是显示的百分比进度条内容
    sys.stdout.write("#")
    # 每次打印的间隔
    time.sleep(1)
    # 从缓存直接刷新出来,一次显示一个
    sys.stdout.flush()
