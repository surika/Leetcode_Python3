class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return None
        ans = []
        tmp = None
        for i in range(numRows):
            a = [1]
            for j in range(i):
                if j == i - 1:
                    a.append(1)
                else:
                    a.append(tmp[j] + tmp[j + 1])
            ans.append(a)
            tmp = a
            a = []
        return ans
