# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        l = 0
        p = head
        while p:
            l += 1
            p = p.next
        index = l//2
        for i in range(0, index):
            head = head.next
        return head

'''
另一种解法：快慢指针法

当用慢指针 slow 遍历列表时，让另一个指针 fast 的速度是它的两倍。
当 fast 到达列表的末尾时，slow 必然位于中间。

复杂度分析

时间复杂度：O(N)，其中 NN 是给定列表的结点数目。
空间复杂度：O(1)，slow 和 fast 用去的空间。
'''
class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
