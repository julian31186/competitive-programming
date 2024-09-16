class Solution:
    def findMinDifference(self, tp: List[str]) -> int:
        res,a = inf,[]
        for i in range(len(tp)):
            x = tp[i].split(":")
            a.append((int(x[0]) , int(x[1])))
        a.sort()
        for i in range(1, len(a)): 
            res = min(res, (a[i][0] - a[i - 1][0]) * 60 + a[i][1] - a[i - 1][1])
        res = min(res, (((23 + a[0][0]) - a[-1][0]) * 60) + (60 - a[i][1]) + a[0][1])
        return res