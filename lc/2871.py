class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        best = nums[0]
        acc = nums[0]
        res = 0
        for i in range(len(nums)):
            acc &= nums[i]
            best = min(best,acc)
        if best != 0: return 1
        acc = nums[0]
        score = 0
        for i in range(len(nums)):
            acc &= nums[i]
            if acc == 0:
                acc = nums[i + 1] if i + 1 < len(nums) else -1
                res += 1 
        return res