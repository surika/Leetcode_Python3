# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 
class Solution:
    total = 0

    def treeSum(self, root):
            if not root:
                return 0
            l = self.treeSum(root.left)
            r = self.treeSum(root.right)
            return l + r + root.val

    def findTilt(self, root: TreeNode) -> int:
        if not root: return 0
        l = self.treeSum(root.left)
        r = self.treeSum(root.right)
        self.total += abs(l - r)
        self.findTilt(root.left)
        self.findTilt(root.right)
        
        return self.total
'''
# 更清晰的题解与写法
使用递归函数 traverse，在任何结点调用该函数，都会返回当前结点下面（包括其自身）的结点和。
借助于任何结点的左右子结点的这一和值，我们可以直接获得该结点所对应的坡度。
'''
class Solution:
    total = 0
    def treeSum(self, root):
            if not root:
                return 0
            l = self.treeSum(root.left)
            r = self.treeSum(root.right)
            self.total += abs(l - r)
            return l + r + root.val

    def findTilt(self, root: TreeNode) -> int:
        self.treeSum(root)
        return self.total