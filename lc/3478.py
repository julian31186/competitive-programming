class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        a = []
        h = []
        p = []
        res = [0] * len(nums1)
        acc = 0
        for i in range(len(nums1)):
            a.append((nums1[i],nums2[i],i))
        a.sort()
        for i in range(len(a)):
            if len(h) > k:
                x = heappop(h)
                acc -= x
            p.append(acc)
            acc += a[i][1]
            heappush(h,a[i][1])
        for i in range(len(a)):
            idx = bisect.bisect_left(a,a[i][0],key = lambda x: x[0])
            res[a[i][2]] = p[idx]
        return res