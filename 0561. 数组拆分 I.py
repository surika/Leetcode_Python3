class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        s = i = 0
        nums.sort()
        while i < len(nums):
            s += nums[i]
            i += 2
        return s