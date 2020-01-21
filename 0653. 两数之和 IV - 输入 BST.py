# BST+链表
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        l = []
        self.pre(root, l)
        p1, p2 = 1, len(l)
        while(p1 < p2):
            if l[p1 - 1] + l[p2 - 1] == k:
                return True
            elif l[p1 - 1] + l[p2 - 1] < k:
                p1 += 1
            elif l[p1 - 1] + l[p2 - 1] > k:
                p2 -= 1
        return False
    def pre(self, root, l):
        if not root:
            return None
        self.pre(root.left, l)
        l.append(root.val)
        self.pre(root.right, l)

#　哈希