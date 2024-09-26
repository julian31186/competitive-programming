class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        res = [0] * len(queries)
        nl,nr,p = [-1] * n,[-1] * n,[]

        for i in range(n):
            if s[i] == "|":
                nl[i] = i
            elif s[i] != "|" and i > 0:
                nl[i] = nl[i - 1]
        
        for i in range(n - 1, -1, -1):
            if s[i] == "|":
                nr[i] = i
            elif s[i] != "|" and i < (n - 1):
                nr[i] = nr[i + 1]
        
        acc = 0
        for i in range(n):
            if s[i] == "|": acc += 1
            p.append(acc)
        
        i = 0
        for u,v in queries:
            l,r = nr[u],nl[v]
            check = p[v] - (p[u - 1] if (u - 1) >= 0 else 0)
            if check > 1:
                res[i] = ((r - l + 1) - (p[r] - (p[l - 1] if l - 1 >= 0 else 0)))
            i += 1
        return res