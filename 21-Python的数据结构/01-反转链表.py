# coding=utf-8
# 反转链表
# 输入: 1->2->3->4->5->Null
# 输出: 5->4->3->2->1->Null

# 关键:当前节点的指针,指向前一个节点
def reverseList(self,head):
    cur, prev = head, None
    while cur:
        # next(a)会依次返回1,2,3,4，StopIteration，StopIteration..
        cur.next, prev, cur = prev, cur, cur.next
    return prev



