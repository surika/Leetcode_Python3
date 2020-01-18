class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l = []
        while n > 0 :
            l.append(n % 10)
            n //= 10
        a = 1
        b = 0
        for i in l:
            a *= i
            b += i
        return a-b