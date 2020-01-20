'''
解决边界问题：
1. 栈 stack 为空： 
    此时 stack.pop() 操作会报错；
    因此，我们采用一个取巧方法，给 stack 赋初值 ? ，
    并在哈希表 dic 中建立 key: '?'，value:'?'的对应关系予以配合。
    此时当 stack 为空且 c 为右括号时，可以正常提前返回 false；
2. 字符串 s 以左括号结尾： 
    此情况下可以正常遍历完整个 s，但 stack 中遗留未出栈的左括号；
    因此，最后需返回 len(stack) == 1，以判断是否是有效的括号组合。

作者：jyd
链接：https://leetcode-cn.com/problems/valid-parentheses/solution/valid-parentheses-fu-zhu-zhan-fa-by-jin407891080/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
# 自己的写法
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(':')', '{':'}', '[':']'}
        for i in s:
            # 左括号
            if i in d.keys():
                stack.append(i)
            # 右括号
            elif len(stack)==0: # 没有多的左括号
                return False 
            elif d.get(stack.pop()) == i:
                continue    
            else: # 弹出的左括号不匹配
                return False
        # 判断是否有未出栈的左括号
        return len(stack) == 0

# 更简洁
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False 
        return len(stack) == 1
