class DSU:
    def __init__(self,n):
        self.p = [-1] * n

    def union(self,a,b):
        i,j = self.find(a),self.find(b)
        if i == j: return
        if self.p[i] > self.p[j]: i,j = j,i
        self.p[i] += self.p[j]
        self.p[j] = i 
    
    def find(self,i):
        if self.p[i] < 0: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    
    def count(self):
        cc = 0
        for x in self.p:
            if x < 0: cc += 1
        return cc
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = DSU(len(s))
        res = [""] * len(s)
        comps = defaultdict(dict)
        for u,v in pairs:
            dsu.union(u,v)
        for i in range(len(s)):
            comps[dsu.find(i)][i] = s[i]
        for k,v in comps.items():
            arr,idx = [],0
            for kk,vv in v.items(): arr.append(vv)
            arr.sort()
            for kk,vv in v.items():
                v[kk] = arr[idx]
                idx += 1
        for k,v in comps.items():
            for kk,vv in v.items():
                res[kk] = vv
        return "".join(res)

        