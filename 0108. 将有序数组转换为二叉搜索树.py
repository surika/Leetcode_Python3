# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums)== 0:return None
        index = len(nums)//2
        root = TreeNode(nums[index])
        l = self.sortedArrayToBST(nums[0:index])
        r = self.sortedArrayToBST(nums[index+1:len(nums)])
        root.left = l
        root.right = r
        return root
