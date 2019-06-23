# coding=utf-8
# 1.输入苹果的单价
price_str = input("苹果的单价:")
# 2.输入苹果的重量
weight_str = input("苹果的重量:")
# 3.计算支付的总金额
# 注意:两个字符串变量之间不能直接使用乘法
money = price_str * weight_str
# 所以需要将价格与重量转为小数再进行计算


# 使用匿名对象进一步简化代码
price = float(input("苹果单价:"))
# 提示用户输入苹果的重量
weight = float(input("苹果的重量:"))
# 计算金额
money1 = price * weight
