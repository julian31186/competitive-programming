class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i,j):
            if not (i >= 0 and i < len(grid2) and j >= 0 and j < len(grid2[0])) or grid2[i][j] == 0: return True
            grid2[i][j] = 0
            flag = True
            if grid1[i][j] != 1: flag = False
            l,r,d,u = dfs(i,j - 1),dfs(i,j + 1),dfs(i + 1,j),dfs(i - 1,j)
            return l and r and d and u and flag
        
        res = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    if dfs(i,j):
                        res += 1
        return res