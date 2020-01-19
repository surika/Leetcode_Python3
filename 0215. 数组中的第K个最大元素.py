# 自己的解法-Pythonic
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

# 堆
# TODO
# 快速选择
# TODO