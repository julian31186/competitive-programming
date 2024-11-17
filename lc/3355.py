class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        a,c = defaultdict(int),0
        for l,r in queries:
            a[(0,l)] += 1
            a[(1,r)] -= 1
        for i in range(len(nums)):
            c += a[(0,i)] if (0,i) in a else 0
            nums[i] -= c
            c += a[(1,i)] if (1,i) in a else 0
        return all(x <= 0 for x in nums)