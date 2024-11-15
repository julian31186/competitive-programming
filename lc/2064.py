class Solution:
    def minimizedMaximum(self, n: int, q: List[int]) -> int:
        res,l,r = inf,1,max(q)
        while l <= r:
            mid,stores = (r + l) // 2,0
            for x in q:
                stores += ceil(x / mid)
                if stores > n: break
            if stores <= n:
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1
        return res