class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        while 0 in nums:
            cnt += 1
            nums.remove(0)
        for _ in range(cnt):
            nums.append(0)