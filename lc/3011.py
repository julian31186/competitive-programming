class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    if nums[j].bit_count() == nums[j + 1].bit_count():
                        nums[j],nums[j + 1] = nums[j + 1],nums[j]
                    else:
                        return False
        return True