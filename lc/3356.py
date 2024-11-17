class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def good(k):
            f,a,c = [],defaultdict(int),0
            for i in range(k):
                l,r,v = queries[i]
                a[(0,l)] += v
                a[(1,r)] -= v
            for i in range(len(nums)):
                c += a[(0,i)] if (0,i) in a else 0
                f.append(c)
                c += a[(1,i)] if (1,i) in a else 0
            return all(f[i] >= nums[i] for i in range(len(nums)))

        l,r,res = 0,len(queries),-1
        while l <= r:
            mid = (r + l) // 2
            if good(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res