class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        res = 0
        dirs = ['N','E','S','W']
        idx = 0
        curr = [0,0]
        obstacles = set([(x,y) for x,y in obstacles])
        for c in commands:
            if c not in [-2,-1]:
                for i in range(c):
                    if idx == 0: 
                        if (curr[0], curr[1] + 1) in obstacles: break
                        curr[1] += 1
                    if idx == 2: 
                        if (curr[0], curr[1] - 1) in obstacles: break
                        curr[1] -= 1
                    if idx == 1: 
                        if (curr[0] + 1, curr[1]) in obstacles: break
                        curr[0] += 1
                    if idx == 3: 
                        if (curr[0] - 1, curr[1]) in obstacles: break
                        curr[0] -= 1
            else:
                if c == -2:
                    idx -= 1
                    if idx < 0: idx = len(dirs) - 1
                if c == -1:
                    idx += 1
                    idx %= 4
            res = max(res,curr[0]**2 + curr[1]**2)
        
        return res