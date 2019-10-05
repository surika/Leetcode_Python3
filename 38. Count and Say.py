# https://leetcode.com/problems/count-and-say/
class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            r = ''
            cnt = 0
            c = s[0]
            for ss in s:
                if ss == c:
                    cnt += 1
                else:
                    r = r + str(cnt) + c
                    c = ss
                    cnt = 1
            if cnt !=  0:
                r = r + str(cnt) + c
            s = r
        return s

#Solution 1 ... using a regular expression

def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    return s
#Solution 2 ... using a regular expression

def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(group)) + digit
                    for group, digit in re.findall(r'((.)\2*)', s))
    return s
#Solution 3 ... using groupby

def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + digit
                    for digit, group in itertools.groupby(s))
    return s