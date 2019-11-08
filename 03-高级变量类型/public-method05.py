# coding=utf-8
# 公共方法即:高级变量共同的方法

# len个数,del()删除变量,max(item)返回容器中元素的最大值(如果是字典,只针对key)
# min(item)返回容器中元素的最小值(如果是字典只针对key比较)
# cmp(item1,item2)比较两个值,-1小于,/0相等,/1大于

# 二.切片,指定索引值的范围,两刀下去得到的结果,就是切片(可以设置步长设置颗粒度)
# 开始索引包含,终止索引包含
# 注意,字典是无序的所以不能切片
Str1 = [0, 1, 2, 3, 4][1:3]
print Str1

# 二
# 列表元组可以通过*号进行重复
# +会生成新列表,但是extend不会生成新列表
# append是直接添加而不是融合

# 三
# in和not in针对列表,字符串,元祖,字典(只能判断key),进行判断在与不在
# 返回true与false

# 四完整的for循环
for num in [1, 2, 3]:
    print (num)
    if num == 2:
        break
else:
    print ("for循环的else是当循环完全结束,就会执行,否则不会")
# 这里顶格就不是for循环内的了,一定执行
print ("循环结束")

# 五,遍历字典的列表,(数组套map)(最常见的对于对象或者说数据库中数据的表示)
students = [
    {"name": "阿土"},
    {"name": "小妹"}
]
# 在学院列表中搜索指定的姓名
find_name = "张三"
for stu_dict in students:
    print (stu_dict)
    if stu_dict["name"] == find_name:
        print ("找到了%s" % find_name)
        # 如果已经找到,应该退出循环,而不再遍历后续元素
        break
    else:
        print ("在if下的else,如果每次条件不成立,都会跳入到这个else中")
# 当列表遍历完全(不能使用break退出循环),我们输出的内容(else)
else:
    print ("抱歉没有找到%s" % find_name)
# 一定会输出的内容
print ("循环结束")
