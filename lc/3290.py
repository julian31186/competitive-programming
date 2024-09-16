class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        @cache
        def dfs(i,cnt,aidx):
            if i == len(b) and cnt < 4: return -inf
            if i == len(b) or cnt == 4: return 0
            take,skip = (a[aidx] * b[i]) + dfs(i + 1,cnt + 1,aidx + 1),dfs(i + 1,cnt,aidx)
            return max(take,skip)
        x = dfs(0,0,0)
        dfs.cache_clear()
        return x