# https://leetcode.com/problems/reverse-words-in-a-string-iii/
class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        y = []
        for i in x:
            t = list(i)
            t.reverse()
            y.append(t)
        r = ' '.join([''.join(i) for i in y])
        return r