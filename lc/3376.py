class Solution:
    def findMinimumTime(self, nums: List[int], K: int) -> int:
        p = list(itertools.permutations(nums))
        res = inf
        for perm in p:
            x = 1
            m = 0
            for i in range(len(perm)):
                m += ceil((perm[i]) / x)
                x += K
            res = min(res, m)
        return res