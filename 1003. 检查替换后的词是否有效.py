# 偷懒用库函数
class Solution:
    def isValid(self, S: str) -> bool:
        while S.find('abc') != -1:
            S = S.replace('abc', '')
        return S ==''
#　栈
class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for i in S:
            if i == 'a':
                stack.append(i)
            elif i == 'b':
                stack.append(i)
            elif i == 'c':
                if len(stack) > 0:
                    if stack.pop() != 'b':
                        return False
                    elif len(stack) > 0:
                        if stack.pop() != 'a':
                            return False
                        else:
                            continue
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0
