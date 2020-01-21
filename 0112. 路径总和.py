'''
方法 1：递归
最直接的方法就是利用递归，遍历整棵树：
如果当前节点不是叶子，对它的所有孩子节点，递归调用 hasPathSum 函数，其中 sum 值减去当前节点的权值；
如果当前节点是叶子，检查 sum 值是否为 0，也就是是否找到了给定的目标和。
'''
class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
'''
方法 2：迭代
算法

我们可以用栈将递归转成迭代的形式。深度优先搜索在除了最坏情况下都比广度优先搜索更快。
最坏情况是指满足目标和的 root->leaf 路径是最后被考虑的，这种情况下深度优先搜索和广度优先搜索代价是相通的。

利用深度优先策略访问每个节点，同时更新剩余的目标和。
所以我们从包含根节点的栈开始模拟，剩余目标和为 sum - root.val。
然后开始迭代：弹出当前元素，如果当前剩余目标和为 0 并且在叶子节点上返回 True；如果剩余和不为零并且还处在非叶子节点上，将当前节点的所有孩子以及对应的剩余和压入栈中。
'''
class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        de = [(root, sum - root.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:  
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False
