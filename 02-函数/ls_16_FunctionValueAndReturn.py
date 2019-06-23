# coding=utf-8

def sum_2_num():
    """"对两个数字的求和(无参函数)"""
    num1 = 10
    num2 = 20
    result = num1 + num2
    print ("%d+%d=%d" % (num1, num2, result))


def sum_2_nums(num1, num2):  # 形参
    """"两个数字的求和(有参版本)"""
    result = num2 + num1
    print ("%d+%d=%d" % (num1, num2, result))


sum_2_nums(1, 2)  # 实参


def sum_2_num_return(num1, num2):
    """"对两个数字的求和并且返回"""
    result = num2 + num1
    # 可以使用返回值,告诉调用函数一方的计算结果
    return result


# 注意需要函数返回的结果需要变量接收接受
sum_reuslt = sum_2_num_return(100, 200)
print ("计算结果为:%d" % sum_reuslt)
