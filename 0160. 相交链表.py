class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        评论区一个很巧妙的方法，使两个链表到达相等位置时走过的是相同的距离
        链表1的长度是x1+y，链表2的长度是x2+y，我们同时遍历链表1和链表2，到达末尾时，再指向另一个链表。
        则当两链表走到相等的位置时：x1+y+x2 = x2+y+x1
        """
        p = headA
        q = headB
        while p!=q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p 