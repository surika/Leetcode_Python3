# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    l = []
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root):
            if not root:return None
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        l = []
        inorder(root)
        for i in range(1, len(l)):
            if l[i-1] >= l[i]:
                return False
        return True


    