class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for l in A:
            l.reverse()
        for l in A:
            for i in range(len(l)):
                if l[i] == 0:
                    l[i] = 1
                else:
                    l[i] = 0
        return A

# 一行版
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    	return [[1 - i for i in i[::-1]] for i in A]

# 另一个快速版
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        """
        :type A: List[List[int]]
        :rtype : List[List[int]]
        """
        output = []
        for index, List in enumerate(A):
            List.reverse()
            targetList = [abs((x-1)) for x in List]
            output.append(targetList)
        return output