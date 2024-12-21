class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l,res = 0,0
        for r in range(2,len(nums)):
            res += ((nums[l] + nums[r]) == (nums[r - 1] / 2))
            l += 1
        return res