# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        d = {}
        def dfs(root):
            if not root:return None
            if root.val in d:
                d[root.val] += 1
            else:
                d[root.val] = 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        m = 0
        ans = set()
        for i in d.keys():
            if d[i] > m:
                ans = set()
                ans.add(i)
                m = d[i]
            if d[i] == m:
                ans.add(i)
        return list(ans)