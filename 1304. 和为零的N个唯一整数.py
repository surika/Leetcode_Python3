# https://blog.csdn.net/sun___M/article/details/83142126
class Solution:
    def sumZero(self, n: int) -> List[int]:
        l = list(range(-int(n/2), int(n/2) + 1))  
        if n % 2 == 0:
            l.remove(0)
        return l