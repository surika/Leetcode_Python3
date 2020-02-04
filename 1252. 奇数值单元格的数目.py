class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        '''
        初始化全0数组的另一种写法
        a = [[0 for _ in range(m)] for j in range(n)]
        注意与a = [0 * m] * n的区别(后一种复制的是地址，改变一个会同步改变)
        '''
        a = []
        for i in range(n):
            b = []
            for j in range(m):
                b.append(0)
            a.append(b)
        for l in indices:
            x = l[0]
            y = l[1]
            for i in range(m):
                a[x][i] += 1
            for j in range(n):
                a[j][y] += 1
        cnt = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] % 2 == 1:
                    cnt += 1
        return cnt