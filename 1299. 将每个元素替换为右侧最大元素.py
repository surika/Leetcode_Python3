class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = [0] * len(arr)
        cur = -1
        for i in range(len(arr)-1, -1, -1):
            l[i] = cur
            if arr[i] > cur:
                cur = arr[i]
        return l
