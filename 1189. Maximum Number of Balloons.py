class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        l = list(text)
        b = ['b', 'a', 'l', 'o', 'n']
        d = {}
        for i in b:
            d[i] = text.count(i)
        d['o'] = d['o'] // 2
        d['l'] = d['l'] // 2
        return min(d.values())