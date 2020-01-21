# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    l = []
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.l = []
        if not root:return None
        self.inorder(root)
        self.l = self.l[::-1]
        pre = None
        for i in self.l:
            node = TreeNode(i)
            node.right = pre
            pre = node
        return pre
        
    def inorder(self, root):
        if not root:
            return None
        self.inorder(root.left)
        self.l.append(root.val)
        self.inorder(root.right)
'''
方法二：中序遍历 + 更改树的连接方式
和方法一类似，我们在树上进行中序遍历，但会将树中的节点之间重新连接而不使用额外的空间。
具体地，当我们遍历到一个节点时，把它的左孩子设为空，并将其本身作为上一个遍历到的节点的右孩子。
'''
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right
