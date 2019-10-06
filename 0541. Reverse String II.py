# https://leetcode.com/problems/reverse-string-ii/
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        li = []
        while(len(s) > 2*k):
            li.append(s[:2*k])
            s=s[2*k:]
        li.append(s)
        r=''
        for e in li:
            ee = e[:k]
            ee.reverse()
            ee += e[k:]
            r += ''.join(ee)
        return r

# Better Solution
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<(k):return s[::-1]
        if len(s)<(2*k):return (s[:k][::-1]+s[k:])
        return s[:k][::-1]+s[k:2*k]+self.reverseStr(s[2*k:],k)