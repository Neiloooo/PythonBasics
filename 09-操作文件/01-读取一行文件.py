# coding=utf-8
file = open("READE.txt")
# 循环判断
while True:
    # 调用文件对象的readline方法一行一行的读
    text = file.readline()
    # 判断是否读取到了内容
    if not text:
        # 读不到了结束循环
        break
    # 否则如果能读到就一直打印输出
    print (text)
# 关闭文件
file.close()
