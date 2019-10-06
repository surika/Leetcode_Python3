# https://leetcode.com/problems/valid-palindrome/
# 判断回文序列
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ss = []
        for i in s:
            if i.isalpha() or i.isdigit(): # 文数字可以用i.isalnum()
                ss.append(i)
        l = 0
        r = len(ss)-1
        while l <= r and ss[l] == ss[r]:
            l += 1
            r -= 1
        if l < r :
            return False
        else:
            return True
            
# 更短更优美！
class Solution:
def isPalindrome(self, s):
    newS= [i.lower() for i in s if i.isalnum()]
    # 天秀
    return newS == newS[::-1]
    #return newS[:len(newS)/2] == newS[(len(newS)+1)/2:][::-1]  # This one is better, but too long