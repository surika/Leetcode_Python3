class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {'R':[1, 0], 'L':[-1, 0], 'U':[0, 1], 'D':[0, -1]}
        acts = [d[m] for m in moves]
        f = list(zip(*acts))
        if sum(f[0]) == 0 and sum(f[1]) == 0:
            return True
        else:
            return False