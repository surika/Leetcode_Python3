# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    total = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.postorder(root)
        return root
    def postorder(self, root) -> int:
        if not root:
            return 0
        tmp = self.postorder(root.right)
        root.val += self.total
        self.total = root.val
        self.postorder(root.left)