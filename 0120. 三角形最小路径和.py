class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dim = len(triangle)
        A = [[9999999 for _ in range(dim)] for _ in range(dim)]
        dp = [[0 for _ in range(dim)] for _ in range(dim)]
        for i in range(dim):
            for j in range(i + 1):
                A[i][j] = triangle[i][j]
        for i in range(dim):
            for j in range(i + 1):
                if i == 0:
                    dp[i][j] = A[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + A[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + A[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + A[i][j], dp[i-1][j] + A[i][j])
        return min(dp[-1])
# 压缩空间到O(n),逆序遍历
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dim = len(triangle)
        dp = [0 for _ in range(dim)]
        for i in range(dim):
            for j in range(i,-1,-1):
                if i == 0:
                    dp[j] = triangle[i][j]
                elif j == 0:
                    dp[j] = dp[j] + triangle[i][j]
                elif j == i:
                    dp[j] = dp[j-1] + triangle[i][j]
                else:
                    dp[j] = min(dp[j-1] + triangle[i][j], dp[j] + triangle[i][j])
        return min(dp)