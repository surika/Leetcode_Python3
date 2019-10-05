# https://leetcode.com/problems/detect-capital/submissions/
# 又是宛如作弊的解法...我爱python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper()==word or word.lower()==word or word.capitalize()==word:
            return True
        else:
            return False

# 更加pythonic的写法：用列表代替多项判断（包括or与if-else）
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
    	return word in [word.upper(), word.lower(), word.title()]
