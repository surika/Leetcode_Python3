# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        total = 0
        stack = []
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if node.val % 2 == 0:
                if node.left and node.left.left:
                    total += node.left.left.val
                if node.left and node.left.right:
                    total += node.left.right.val
                if node.right and node.right.left:
                    total += node.right.left.val
                if node.right and node.right.right:
                    total += node.right.right.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return total

