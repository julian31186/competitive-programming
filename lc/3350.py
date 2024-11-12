class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        res,cnt,prev = 0,1,0
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                cnt += 1
            else:
                prev = cnt
                cnt = 1
            
            res = max(res,min(prev,cnt),cnt // 2 if cnt % 2 == 0 else 0)
        return res