# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 递归
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        l = []
        self.postorder(root, l)
        return l
    def postorder(self, root, l):
        if not root:
            return None
        self.postorder(root.left, l)
        self.postorder(root.right, l)
        l.append(root.val)
# 迭代