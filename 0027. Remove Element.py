class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        r = len(nums) - 1
        for n in nums:
            if n != val:
                cnt += 1
        if cnt == 0:
            return cnt
        for i in range(len(nums)):
            while nums[r] == val:
                r = r - 1
            if nums[i] == val and i <= r:
                nums[i] = nums[r]
                nums[r] = val
            else:
                continue
        return cnt

# Simpler Solution
class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)