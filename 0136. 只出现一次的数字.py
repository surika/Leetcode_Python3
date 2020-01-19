class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i]==nums[i+1]:
                i = i + 2
            else:
                break
        return nums[i]
'''
推荐解法:按位异或
'''