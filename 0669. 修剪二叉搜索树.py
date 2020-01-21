'''
方法：递归

思路
令 trim(node) 作为该节点上的子树的理想答案。我们可以递归地构建该答案。

算法
当 node.val > R，那么修剪后的二叉树必定出现在节点的左边。
类似地，当 node.val < L，那么修剪后的二叉树出现在节点的右边。否则，我们将会修剪树的两边。
'''
class Solution(object):
    def trimBST(self, root, L, R):
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)
