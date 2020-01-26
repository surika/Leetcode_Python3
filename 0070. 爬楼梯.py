# DP
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        for i in range(0, 3):
            dp[i] = i
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

# 可以只储存dp[i-1]和dp[i-2]，空间复杂度降到O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            a = 1
            b = 2
            for i in range(3, n):
                a, b = b, a + b
        return a + b
