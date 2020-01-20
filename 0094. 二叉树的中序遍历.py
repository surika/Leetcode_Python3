# 递归
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        l = []
        self.inorder(root, l)
        return l
    def inorder(self, root, l):
        if not root:
            return None
        self.inorder(root. left, l)
        l.append(root.val)
        self.inorder(root.right, l)
# 迭代