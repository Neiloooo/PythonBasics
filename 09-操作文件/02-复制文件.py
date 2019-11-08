# coding=utf-8
# 1.打开
file_read = open("READE.txt")
# 这里修改打开文件的状态为只写
file_write = open("READE[1]", "w")

# 2.读,写
while True:
    # 读取一行内容
    text = file_read.readline()
    # 判断是否读取到内容
    if not text:
        break
    file_write.write(text)

# 3.关闭
file_read.close()
file_write.close()
