# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 访问节点值前必须判断节点是否存在
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        h = head
        while head and head.next:
            p = head.next
            while p and head.val == p.val: # 注意判断p节点是否存在
                p = p.next
            head.next = p
            head = head.next
        return h

# 变量更精简
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        h = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return h