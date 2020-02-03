class Solution:
    def permute(self, nums):
        def backtrack(first = 0):
            if first == n:  # if all integers are used up
                output.append(nums[:])
            for i in range(first, n):   
                nums[first], nums[i] = nums[i], nums[first]  # place i-th integer first # in the current permutation
                backtrack(first + 1) # use next integers to complete the permutations
                nums[first], nums[i] = nums[i], nums[first] # backtrack
        n = len(nums)
        output = []
        backtrack()
        return output