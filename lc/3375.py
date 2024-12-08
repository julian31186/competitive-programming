class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(x < k for x in nums): return -1
        nums = sorted(list(set(nums)))
        return len(nums) - bisect_right(nums,k)