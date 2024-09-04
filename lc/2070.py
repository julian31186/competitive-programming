class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        c = defaultdict(int)
        arr = []
        res = []
        for p,b in items:
            c[p] = max(c[p],b)
        for k,v in c.items():
            arr.append([k,v])
        acc = 0
        for i in range(len(arr)):
            acc = max(acc,arr[i][1])
            arr[i][1] = acc
        for i in range(len(queries)):
            l,r = 0,len(arr) - 1
            best = 0
            while l <= r:
                m = (r + l) // 2
                p,b = arr[m]
                if p <= queries[i]:
                    best = max(best,b)
                    l = m + 1
                else:
                    r = m - 1
            res.append(best)
        return res