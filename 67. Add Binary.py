# string
# https://leetcode.com/problems/add-binary/submissions/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = max(len(a), len(b))
        a = a.zfill(l)
        b = b.zfill(l)
        plus = 0
        result = ""
        for i in range(l-1,-1,-1):
            if int(a[i]) + int(b[i]) + plus == 0:
                result = '0' + result 
                plus = 0
            elif int(a[i]) + int(b[i]) + plus == 1:
                result = '1' + result 
                plus = 0
            elif int(a[i]) + int(b[i]) + plus == 2:
                result = '0' + result 
                plus = 1
            elif int(a[i]) + int(b[i]) + plus == 3:
                result = '1' + result 
                plus = 1
        if plus == 1:
            result = '1' + result 
        if len(result) > 1:
            result = result[result.index('1'):]
        return result