# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in d.keys():
            if d[i] > len(nums)/2:
                return i

#
class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		'''
		Collections is a library with very fast Python data structures. Defaultdict is on of them with default values for new keys.
		'''
		d = defaultdict(int)        # default dict with 0 values for every new key
		for num in nums:        # for every number
			d[num] += 1     # add value of its key by 1
			
		return max(d, key=d.get)        # return key with the biggest value