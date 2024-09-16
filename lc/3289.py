class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        vis = set()
        res = []
        for i in range(len(nums)):
            if nums[i] in vis: res.append(nums[i])
            vis.add(nums[i])
        return res