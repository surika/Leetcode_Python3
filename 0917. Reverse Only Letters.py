class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        d = {}
        li = []
        ls = list(S)
        for i in range(len(ls)):
            if ls[i].isalpha():
                li.append(i)
        la = [ls[i] for i in li]
        la.reverse()
        cnt = 0
        for i in li:
            ls[i] = la[cnt]
            cnt += 1
        ss = "".join(ls)
        return ss
        