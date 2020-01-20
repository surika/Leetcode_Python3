# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        h = ListNode(None)
        ph = h
        while head and head.next:
            f = False
            while head.val == head.next.val:
                f = True
                head = head.next
            if f:
                ph.next = head.next
            else:
                ph.next = head
            ph = ph.next
                head = head.next
        return h.next