class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        a = b = 0
        for i in range(len(nums) - 1):
            a, b = b, max(a + nums[i], b)
        tmp1 = b
        a = b = 0
        for i in range(1, len(nums)):
            a, b = b, max(a + nums[i], b)
        tmp2 = b
        return max(tmp1, tmp2)