class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []#奇数
        odd = [] #偶数
        for i in A:
            if i % 2 == 1:
                even.append(i)
            else :
                odd.append(i)
        return odd + even