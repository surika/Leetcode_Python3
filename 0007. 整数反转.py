class Solution:
    def reverse(self, x: int) -> int:
        f = True # 默认为非负数
        if x < 0:
            f = False # 负数
            x *= (-1)
        result = 0
        while x > 0:
            result = result * 10 + (x % 10)
            x //= 10
        if not f:
            result = -result
        # 注意审题。要求是翻转后溢出，故判断应在最末尾
        if result < -2**31 or result > 2**31-1:
            return 0
        return result