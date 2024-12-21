class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        R,C,MOD = len(grid),len(grid[0]),10**9 + 7
        @cache
        def dfs(i,j,acc):
            if not (i >= 0 and i < R and j >= 0 and j < C): return 0
            if (acc ^ grid[i][j] == k) and ((i == R - 1) and (j == C - 1)): return 1
            res = 0
            acc ^= grid[i][j]
            res += dfs(i + 1,j,acc) % MOD
            res += dfs(i,j + 1,acc) % MOD
            return res % MOD
        x = dfs(0,0,0)
        dfs.cache_clear()
        return x