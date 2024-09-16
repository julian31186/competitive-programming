class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
        vis = set()
        @cache
        def dfs(i,j,h):
            if (not (i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]))) or ((i,j) in vis): 
                return False
            if grid[i][j] == 1: h -= 1
            if h == 0: return False
            if (i,j) == (len(grid) - 1,len(grid[0]) - 1): return True
            vis.add((i,j))
            d,u,r,l = dfs(i + 1,j,h),dfs(i - 1,j,h),dfs(i,j + 1,h),dfs(i,j - 1,h)
            vis.remove((i,j))
            return d or u or r or l
        return dfs(0,0,health)