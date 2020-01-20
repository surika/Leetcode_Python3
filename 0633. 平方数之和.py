# 双指针
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c ** 0.5)
        res = a ** 2 + b ** 2
        while a <= b:
            if res == c:
                return True
            elif res < c:
                a += 1
            else:
                b -= 1
            res = a ** 2 + b ** 2
        return False
