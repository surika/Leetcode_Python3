class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)