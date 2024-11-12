class Solution:
    def maximumBeauty(self, a: List[List[int]], queries: List[int]) -> List[int]:
        res,acc = [],0
        a.sort()
        for i in range(len(a)):
            acc = max(acc,a[i][1])
            a[i][1] = acc
        for q in queries:
            x = bisect_right(a,q,key=lambda x: x[0]) - 1
            res.append(a[x][1] if x != -1 else 0)
        return res