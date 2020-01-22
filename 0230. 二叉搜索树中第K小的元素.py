# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    cnt = 0
    ans = 0
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:return None
        
        def preorder(root):
            if not root:
                return None
            if self.cnt == k:
                return None
            preorder(root.left)
            self.cnt += 1
            if self.cnt == k:
                self.ans = root.val
            preorder(root.right)
        preorder(root)
        return self.ans