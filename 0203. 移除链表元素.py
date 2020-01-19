# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        h = ListNode(None)
        h.next = head
        pre = h
        while head:
            if head.val == val:
                head = head.next
            else:
                pre.next = head
                pre = head
                head = head.next
        pre.next = head
        return h.next