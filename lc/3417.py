class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res,f,b = [],False,False
        for i in range(len(grid)):
            if f:
                for j in range(len(grid[0]) - 1, -1, -1):
                    b = not b
                    if b:
                        res.append(grid[i][j])
                    
                f = not f
            else: 
                for j in range(0,len(grid[0])):
                    b = not b
                    if b:
                        res.append(grid[i][j])
                f = not f
        return res