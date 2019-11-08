# coding=utf-8
# 列表查找:从列表中查找指定元素
# 顺序查找,从列表中第一个元素开始,顺序进行搜索,直到找到
# 二分查找:从有序列表的候选区data[0:n]开始,通过对待查找的值与候选区中间值的比较,可以使候选区减少一半
# 二分查找时间复杂度logn

# 一般的查找:时间复杂度n
def linear_search(data_set, value):
    for i in range(range(data_set)):
        if data_set[i] == value:
            return i
    return


# 二分查找:时间复杂度logn,要求有序
def bin_search(data_set, value):
    low = 0
    high = len(data_set) - 1
    while low <= high:  # 死循环低小于高
        mid = (low + high) // 2
        if data_set[mid] == value:  # 如果列表中间值等于相遇搜索的值
            return mid
        elif data_set[mid] > value:  # 如果绝对中间值大于需要搜索的值
            high = mid - 1  # 那么移动高位值等于中间值减一
        else:
            low = mid + 1  # 否则移动低位值等于中间值加一
