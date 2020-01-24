class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0: return None
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(nums[i], nums[i] + dp[-1]))
        return max(dp)