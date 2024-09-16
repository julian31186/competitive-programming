class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        res,pre = [],[]
        cc = Counter()
        for i,c in enumerate(s):
            cc[c] += 1
            pre.append(cc.copy())
        for u,v,c in queries:
            curr = pre[v] - pre[u - 1] if u - 1 >= 0 else pre[v]
            odd = sum(1 for v in curr.values() if v % 2 != 0)
            if c >= (odd // 2): res.append(True)
            else: res.append(False)
        return res