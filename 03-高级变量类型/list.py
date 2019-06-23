# coding=utf-8
import json

# 列表,相当于java的数组
# 最长应用场景:存储相同类型的数据,然后通过迭代遍历,再循环体内部,
# 针对列表中的每一项元素,执行相同的操作
name_list = ["zhangsan", "lisi", "wangwu"]
print (name_list)
# 通过索引取出列表中的数据,以索引从0开始
print (name_list[1])

# 1.取值和取索引,且注意不要超出索引范围
print (name_list[0])
# 根据列表中的内容取索引值,但是如果输入的内容列表中没有会报错
print (name_list.index("lisi"))

# 2.修改
name_list[1] = "wangermazi"
# 3.增加,append可以向列表的末尾追加数据
name_list.append("wangxiaoer")
# 3.1 insert方法可以在索引2的指定位置插入数据
name_list.insert(1, "张三")

print json.dumps(name_list, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)

# 4.删除列表中的元素
# 删除指定元素
name_list.remove("张三")
# 删除列表中最后的元素或指定元素
name_list.pop()
name_list.pop(0)
# clear方法可以清空列表2.7没有clear方法

# 5.del关键字,同样可以删除指定元素
del name_list[1]
# del关键字本质上是用来将一个变量从内存中删除的
nam = "小明"
del nam
# 注意,如果使用del关键字将变量从内存中删除
# 后续的代码就不能再使用这个变量了

# 6.count关键字,可以统计列表中某一个数据出现的次数
count = name_list.count("张三")
print ("张三出现了%d次" % count)

# 7.sort排序,三个参数:默认升序
name_list.sort()
# 降序
name_list.sort(reverse=True)

# 8.列表的遍历(for循环)
for my_name in name_list:
    print ("我的名字叫%s" % my_name)
