# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = 99999
    def minDepth(self, root: TreeNode) -> int:
        if not root:return 0
        def helper(root, depth):
            if not root:return
            if not root.left and not root.right:
                if depth < self.ans:
                    self.ans = depth
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        helper(root, 1)
        return self.ans