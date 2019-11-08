# coding=utf-8
# 排序的最弱组合:
# 1.冒泡排序:列表每两个相邻的数,如果前边的比后边的大,那么交换这两个数,复杂度n方
def bubble_sort(li):
    for i in range(len(li) - 1):  # i表示第几趟,十个数如果使用冒泡排序,需要走9趟才能完成排序
        for j in range(len(li) - i - 1):  # j表示图中的箭头
            if li[j] > li[j + 1]:  # 如果当前箭头指向的数大于J+1,那么双方数互换
                li[j], li[j + 1] = li[j + 1], li[j]


# 冒泡排序优化版本-如果执行一趟没有任何交换,则已经是有序,可以直接结束算法

# 2.选择排序:一趟遍历记录最小的数,放到第一个位置,再一趟遍历记录剩余列表中最小的数,继续放置 复杂度:CN2
def selcet_sort(li):
    for i in range(len(li) - 1):
        # 第i趟开始时,无序区: li[i:]
        # 找无序区最小值,保存最小值的位置
        min_pos = i  # min_pos保存最小值的位置
        for j in range(i + 1, len(li)):
            if li[j] < li[min_pos]:
                min_pos = j
            li[min_pos], li[i] = li[i], li[min_pos]


# 3.插入排序:列表被分为有序区和无序区两个部分,最初有序区只有一个元素.每次从无序区选择一个元素,插入到有序区的部分,直到无序区变为空
def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1  # j是手里最后一张牌的下标
        while j >= 0 and li[j] > tmp:  # 两个终止条件: j小于0表示tmp顺序最小的,顺序不能乱
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp


