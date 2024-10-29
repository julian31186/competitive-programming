class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        def valid(i,j):
            return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

        @cache
        def dp(i,j):
            r = 1 + dp(i,j + 1) if valid(i,j + 1) and grid[i][j + 1] > grid[i][j] else 0
            br = 1 + dp(i + 1,j + 1) if valid(i + 1,j + 1) and grid[i + 1][j + 1] > grid[i][j] else 0
            tr = 1 + dp(i - 1,j + 1) if valid(i - 1,j + 1) and grid[i - 1][j + 1] > grid[i][j] else 0
            return max(r,br,tr)
    
        return max([dp(i,0) for i in range(len(grid))])