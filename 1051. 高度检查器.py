class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        source = [i for i in heights]
        heights.sort()
        cnt = 0
        for i in range(len(heights)):
            if source[i] != heights[i]:
                cnt += 1
        return cnt