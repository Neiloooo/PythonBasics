# coding=utf-8
# 字典通常用来存取无序的数据集合,键值对(Map)
# 而且key必须是唯一的,通常输出的顺序与定义的顺序是不一致的
xiaoming_dict = {"name": "xiaoming",
                 "aget": 19}
print (xiaoming_dict)
# 1.取值,根据key值获取value值
print (xiaoming_dict["name"])

# 2.增加/修改
xiaoming_dict["gender"] = 0
# 2.1如果key存在,会修改已经存在的键值对
xiaoming_dict["name"] = "xiaoxiaoming"

# 3.删除
# 指定要删除的键值对的键值,即可使用pop方法删除
xiaoming_dict.pop("name")

# 1.统计键值对的数量
print (len(xiaoming_dict))
# 2.合并字典(将新的字典,合并(添加)进入一个新的字段)
# 如果被合并的字典汇总包含已存在的键值对,那么就会覆盖已有的键值对
temp_dict = {"aget": 20}
xiaoming_dict.update(temp_dict)
# 3.清空字典
xiaoming_dict.clear()

# 循环遍历字典for循环:
# 变量k是每一次循环汇总,获取到的键值对的key
for k in xiaoming_dict:
    print ("%s-%s" % [k, xiaoming_dict[k]])

# 一般的使用场景,列表套字典,就像集合套Map一样,一个Map就是一条数据
card_list = [
    {
        "name": "张三",
        "qq": "12345",
        "phone": "1100"
    },
    {
        "name": "李四",
        "qq": "514121",
        "phone": "12312"
    }
]
for card_info in card_list:
    print (card_info)
