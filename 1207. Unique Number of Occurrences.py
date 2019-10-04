class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        s = set(arr)
        for i in s:
            dic[i] = 0
        for i in arr:
            dic[i] += 1
        if len(s) == len(set(dic.values())):
            return True
        else:
            return False
        