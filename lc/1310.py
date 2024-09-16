class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res,p = [],[]
        acc = 0
        for i in range(len(arr)):
            acc ^= arr[i]
            p.append(acc)
        for u,v in queries:
            res.append(p[v] ^ p[u - 1] if u - 1 >= 0 else p[v])
        return res 