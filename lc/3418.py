class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        r,c = len(coins),len(coins[0])
    
        @cache
        def dp(i,j,ability):
            if (i == r) and (j == c - 1) or (j == c and i == r - 1): return 0
            if not (i >= 0 and i < r and j >= 0 and j < c): return -inf
            res = -inf
            res = max(res, coins[i][j] + dp(i + 1,j,ability), coins[i][j] + dp(i,j + 1,ability))
            if coins[i][j] < 0 and ability > 0:
                res = max(res, dp(i + 1,j,ability - 1), dp(i,j + 1,ability - 1))
            return res

        x = dp(0,0,2)
        dp.cache_clear()
        return x