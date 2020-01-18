# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l11, l22 = l1, l2
        while l1.next and l2.next:
            l1, l2 = l1.next, l2.next
        while l1.next:
            l1 = l1.next
            l2.next = ListNode(0)
            l2 = l2.next
        while l2.next:
            l2 = l2.next
            l1.next = ListNode(0)
            l1 = l1.next
        
        plus = 0
        p = ListNode(None)
        head = p
        l1, l2 = l11, l22
        while l1 and l2:
            v = l1.val + l2.val + plus
            plus = v // 10
            n = ListNode(v % 10)
            p.next = n
            p = p.next
            l1, l2 = l1.next, l2.next
        if plus == 1:
            p.next = ListNode(1)
        return head.next

#---
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)
        r=re
        carry=0
        while(l1 or l2):
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0
            s=carry+x+y
            carry=s//10
            r.next=ListNode(s%10)
            r=r.next
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        if(carry>0):
            r.next=ListNode(1)
        return re.next