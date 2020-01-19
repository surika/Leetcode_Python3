# 哈希
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = [i]
            else:
                m[nums[i]].append(i)
                if m[nums[i]][-1] - m[nums[i]][-2] <= k:
                    return True
        return False