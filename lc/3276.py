class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        arr = [[] for i in range(100)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                arr[grid[i][j] - 1].append(i)
        
        @cache
        def dfs(idx,mask):
            if idx == 100: return 0
            res = 0
            for i in range(len(arr[idx])):
                if (1 << arr[idx][i]) & mask == 0:
                    res = max(res,idx + 1 + dfs(idx + 1, mask | (1 << arr[idx][i])))
            res = max(res, dfs(idx + 1, mask))
            return res
        
        return dfs(0,0)
    