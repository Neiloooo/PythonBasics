# coding=utf-8
# 如果a+b+c=1000,且a^2+b^2=c^2(abc为自然数),如何求出范围内所有abc的组合
# 1.穷举算法
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print "a,b,c:%d,%d,%d" % (a, b, c)
# 2.优化穷举算法,C不是穷举得出,而是通过a和b直接得出
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a**2+b**2== c**2:
            print "a,b,c:%d,%d,%d" % (a, b, c)
