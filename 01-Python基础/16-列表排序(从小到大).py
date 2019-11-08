# -*-  coding:utf-8 -*-
from decimal import *
list = [3, 56, 54, 67, 88, 999, 556, 1]


def mySort(list):
    newList = []
    for i in range(len(list)):
        number = min(list)
        newList.append(number)
        list.remove(number)
    return newList


result = mySort(list)
print(result)




def sort_new(a,b,c):
    a = Decimal(a)
    b = Decimal(b)
    c= Decimal(c)
    list=[]
    if a-b>0:
        a,b=b,a
    if b-c>0:
        b,c=c,b
    if a-b>0:
        a,b=b,a

    return a,b,c
    # list.append(a)
    # list.append(b)
    # list.append(c)
print(sort_new(2.22222,3.111111,1.2222222))
print(sort_new(27.0000,21.1211,3.00032))
