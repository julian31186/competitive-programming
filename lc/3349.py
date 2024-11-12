class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(0,len(nums) - (k * 2) + 1):
            f = True
            for j in range(i + 1,i + k):
                if nums[j] <= nums[j - 1]: 
                    f = False
                    break
            for j in range(i + k + 1,i + k + k):
                if nums[j] <= nums[j - 1]: 
                    f = False
                    break
            if f: return True
        return False