# 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        l = []
        while head.next:
            if head in l:
                return True
            l.append(head)
            head = head.next
        return False
# 快慢指针
class Solution(object):
	def hasCycle(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		if not (head and head.next):
			return False
		#定义两个指针i和j，i为慢指针，j为快指针
		i,j = head,head.next
		while j and j.next:
			if i==j:
				return True
			# i每次走一步，j每次走两步
			i,j = i.next, j.next.next
		return False
