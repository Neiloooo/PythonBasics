# coding=utf-8
# While循环的使用

# 三大流程:循序,分支(if,else),循环(while)
# 循环:打印996五遍
i = 1
while i <= 5:
    # 1>希望在循环内执行的代码
    print ("996,icu")
    # 处理计数器i
    i = i + 1
# 3.查看循环结束后,技术器i的数值是多少
print ("循环结束,i=%d" % i)

# 死循环:,忘记在循环内部修改循环的判断条件,形成永远成立的条件,导致程序无法终止

# 赋值运算符的使用:
# c=a+b是将a+b的运算结果赋值到C上
# c+=a等效于c=c+a
# c-=a等效于c=c-a
# 这样i=i+1等效于i+=1

# 循环计算:
# 案例一:0-100之间的数字累计求和
result = 0
i = 0
while i <= 100:
    print (i)
    # 每次循环,都让result这个变量和i这个计数器相加
    result += i
    # 处理计数器
    i += 1
print ("0-100之间的数字求和结果=%d" % result)

# 案例二:计算0到100之间的偶数求和
result01 = 0
j = 0
while j <= 100:
    if j % 2 == 0:
        print (j)
        result01 += j
    j += 1
print ("0-100之间的偶数求和为=%d" % result01)
