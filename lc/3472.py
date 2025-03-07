class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:

        @cache
        def dist(a,b):
            a,b = sorted([a,b])
            return min(
                (ord(a) - ord('a')) + (26 - (ord(b) - ord('a'))),
                (ord(b) - ord('a')) - (ord(a) - ord('a'))
            )
            
        @cache
        def dp(i,j,k):
            if i > j: return 0
            if i == j: return 1
            res = 0
            if s[i] == s[j]:
                res = max(res, 2 + dp(i + 1,j - 1, k))
            else:
                d = dist(s[i],s[j])
                if d <= k:
                    res = max(res, 2 + dp(i + 1,j - 1, k - d))
                res = max(res, dp(i + 1,j,k), dp(i,j - 1,k))
            return res
        
        x = dp(0,len(s) - 1,k)
        dp.cache_clear()
        return x