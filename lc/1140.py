class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        @cache
        def dfs(i,M,alice):
            if i == len(piles): return 0
            res = 0 if alice else inf
            stones_taken = 0
            bob = not alice
            for X in range(1,2 * M + 1):
                if i + X - 1 >= len(piles): break
                stones_taken += piles[i + X - 1]
                if alice:
                    res = max(res, stones_taken + dfs(i + X, max(X,M), False))
                elif bob:
                    res = min(res, dfs(i + X, max(X,M), True))
            return res

        return dfs(0,1,True)