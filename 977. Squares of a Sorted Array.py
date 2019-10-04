#https://leetcode.com/problems/squares-of-a-sorted-array/submissions/
# 这个解法简直太偷懒了宛如作弊...但是我喜欢！Python大法好！
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        a = [i * i for i in A]
        a.sort()
        return a

# 更简洁的写法
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
    	return sorted(i*i for i in A)