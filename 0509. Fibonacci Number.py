# https://leetcode.com/problems/fibonacci-number/
# 本来想用递归，但是注意到0 <= N <= 30，因此打表即可
class Solution:
    def fib(self, N: int) -> int:
        f = {}
        f[0] = 0
        f[1] = 1
        # 此处31可以优化为N+1，减少不必要的计算
        for i in range(2,31):
            f[i] = f[i-1] + f[i-2]
        return f[N]
    
# TODO:动态规划解法
class Solution:
    def fib(self, N: int) -> int:
        fibonacci = [0, 1]
        fibonacci += ([0] * (N - 1))  # Grow the list accordingly if N is larger than 1
        
        i = 2
        while i <= N:               # Calculate values of the sequence in ascending order
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]   
            i += 1
        return fibonacci[N]