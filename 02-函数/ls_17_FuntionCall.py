# coding=utf-8
def test1():
    print ("炒房兴邦")


def test2():
    print ("实业误国")
    # 函数的嵌套调用,本类中的函数可以直接调用
    test1()
    print ("别问,问就是996")


def print_line(char, times):
    """"定义打印五次任意值的函数"""
    print (char * times)


def print_lines(char, times):
    """"打印五次996ICU,横着与竖着都是五,横着我们可以调用以写函数"""
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1


print_lines("996,ICU", 5)
