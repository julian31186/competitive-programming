class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        best,acc,lgst,res = max(nums),(2**32) - 1,0,0
        for i in range(len(nums)):
            acc &= nums[i]
            if acc < best:
                acc = (2**32) - 1
                lgst = 0
            else:
                lgst += 1
            res = max(res,lgst)
        return res