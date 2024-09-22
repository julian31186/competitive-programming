class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        res = 0

        for i in range(len(grid)):
            reg = ""
            inv = ""
            for j in range(len(grid[0])):
                reg += str(grid[i][j])
            for j in range(len(reg)):
                inv += "0" if reg[j] == "1" else "1"
            reg,inv = int(reg,2),int(inv,2)
            if reg > inv: continue
            else:
                for j in range(len(grid[0])):
                    grid[i][j] = 1 if grid[i][j] == 0 else 0

        for j in range(len(grid[0])):
            zero,one = 0,0
            for i in range(len(grid)):
                if grid[i][j] == 0: zero += 1
                else: one += 1
            if zero > one:
                for i in range(len(grid)):
                    grid[i][j] = 1 if grid[i][j] == 0 else 0
        
        for i in range(len(grid)):
            curr = ""
            for j in range(len(grid[0])):
                curr += str(grid[i][j])
            res += int(curr,2)
        
        return res