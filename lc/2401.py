class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l,res,acc = 0,0,0
        for r in range(len(nums)):
            while l < r and acc & nums[r] != 0:
                acc ^= nums[l]
                l += 1
            acc |= nums[r]
            res = max(res, r - l + 1)
        return res