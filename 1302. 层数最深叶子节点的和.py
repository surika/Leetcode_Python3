# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    maxdepth = 0
    total = 0
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # maxdepth = 0
        # total = 0
        self.dfs(root, 0)
        return self.total

    def dfs(self, root, depth):
        if not root:
            return None
        if depth > self.maxdepth:
            self.maxdepth = depth
            self.total = root.val
        elif depth == self.maxdepth:
            self.total += root.val
        self.dfs(root.left, depth+1)
        self.dfs(root.right, depth+1)