# top-down 暴力
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#自己的解法(top-down)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        if not root:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        return max(lh, rh)+1

'''
从底至顶（提前阻断法）
对二叉树做深度优先遍历DFS，递归过程中：
终止条件：当DFS越过叶子节点时，返回高度0；
返回值：
从底至顶，返回以每个节点root为根节点的子树最大高度(左右子树中最大的高度值加1max(left,right) + 1)；
当我们发现有一例 左/右子树高度差 ＞ 1 的情况时，代表此树不是平衡树，返回-1；
当发现不是平衡树时，后面的高度计算都没有意义了，因此一路返回-1，避免后续多余计算。
最差情况是对树做一遍完整DFS，时间复杂度为 O(N)。
'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.depth(root) != -1

    def depth(self, root):
        if not root: return 0
        left = self.depth(root.left)
        if left == -1: return -1
        right = self.depth(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1

'''
从顶至底（暴力法）
构造一个获取当前节点最大深度的方法 depth() ，通过比较左右子树最大高度差abs(self.depth(root.left) - self.depth(root.right))，来判断以此节点为根节点下是否是二叉平衡树；
从顶至底DFS，以每个节点为根节点，递归判断是否是平衡二叉树：
若所有根节点都满足平衡二叉树性质，则返回 True ；
若其中任何一个节点作为根节点时，不满足平衡二叉树性质，则返回False。
本方法产生大量重复的节点访问和计算，最差情况下时间复杂度 O(N^2)。
'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
