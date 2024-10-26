class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:

        @cache
        def dp(idx,s):
            if s == k: return 0
            res = 0
            for i in range(n):
                if i == idx: res = max(res,stayScore[s][idx] + dp(i,s + 1))
                else: res = max(res,travelScore[idx][i] + dp(i,s + 1))
            return res
  
        res = 0
        for i in range(n):
            x = dp(i,0)
            res = max(res,x)
        return res