class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res,vis = 0,set(nums)
        for i in range(len(nums)):
            if nums[i] - 1 not in vis:
                curr = nums[i]
                check = 0
                while curr in vis:
                    curr += 1
                    check += 1
                res = max(res,check)
        return res