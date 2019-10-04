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