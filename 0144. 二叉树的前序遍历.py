# 递归
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        l = []
        self.preorder(root, l)
        return l

    def preorder(self, root, l):
        if not root:
            return None
        l.append(root.val)
        self.preorder(root.left, l)
        self.preorder(root.right,l)

# 迭代-使用栈
# 注意迭代时入栈顺序与遍历顺序相反,先右再左
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        stack = []
        l = []
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            l.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return l

# 莫里斯遍历-O(n)时间, O(1)空间