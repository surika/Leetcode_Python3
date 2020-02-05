"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        cur_level = [root]
        while cur_level:
            tmp = []
            next_level = []
            for node in cur_level:
                tmp.append(node.val)
                if node.children:
                    next_level.extend(node.children)
            res.append(tmp)
            cur_level = next_level
        return res