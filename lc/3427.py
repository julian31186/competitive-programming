class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            acc = 0
            for j in range(start,i + 1):
                acc += nums[j]
            res += acc
        return res