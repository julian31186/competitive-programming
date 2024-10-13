class Solution:
    def countWinningSequences(self, s: str) -> int:
        MOD = 10**9 + 7
        c = { "WE": -1, "WF": 1, "WW": 0, "EE": 0, "EF": -1, "EW": 1, "FE": 1, "FF": 0, "FW": -1 }

        @cache
        def dfs(i,bobs,prev):
            if i == len(s):
                if bobs > 0: return 1
                else: return 0
            res = 0
            for x in "WFE":
                if x == prev: continue
                res += (dfs(i + 1,bobs + c[x + s[i]],x) % MOD)
            return res % MOD 

        return dfs(0,0,"")