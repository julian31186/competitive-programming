class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:

        half = len(cost) // 2
        
        @cache
        def dp(delta,p1,p2):
            if delta == half:
                return 0
            res = inf
            for i in range(3):
                for j in range(3):
                    if (i != j) and (i != p1) and (j != p2):
                        res = min(res, cost[delta][i] + cost[len(cost) - delta - 1][j] + dp(delta + 1,i,j))
            return res

        x = dp(0,-1,-1)
        dp.cache_clear()
        return x