# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归
class Solution:
    ans = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        self.depth(root)
        return self.ans

    def depth(self, root):
        if not root:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        if (l + r) > self.ans: self.ans = (l + r)
        return max(l, r) + 1

# 详细题解:https://leetcode-cn.com/problems/diameter-of-binary-tree/solution/hot-100-9er-cha-shu-de-zhi-jing-python3-di-gui-ye-/

# 迭代
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = []
        stack.append(root)
        while len(stack)>0:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root