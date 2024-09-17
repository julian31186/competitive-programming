class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        for i in range(len(nums)):
            nums[i] %= value
        c = defaultdict(int)
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] += (value * c[nums[i]])
            c[temp] += 1
        nums.sort()
        idx = 0
        for i in range(len(nums)):
            if nums[i] != idx: return idx
            else: idx += 1
        return idx