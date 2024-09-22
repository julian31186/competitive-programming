class Solution:
    def minNumberOfSeconds(self, mh: int, wt: List[int]) -> int:
        res = 0
        h = []
        for i in range(len(wt)):
            heappush(h,(wt[i],1,wt[i]))
        while mh > 0:
            time,num,base = heappop(h)
            n = num + 1
            new_time = base * ((n * (n + 1)) // 2)
            mh -= 1
            res = max(res,time)
            heappush(h,(new_time,n,base))
        return res