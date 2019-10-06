class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        p = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[p]:
                continue
            nums[p+1] = nums[i]
            p = p + 1
        return p + 1
