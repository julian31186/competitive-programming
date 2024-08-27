class Solution:
    def getFinalState(self, nums: List[int], k: int, m: int) -> List[int]:
        def good():
            res,idx = inf,-1
            for i in range(len(nums)):
                if nums[i] < res:
                    res = nums[i]
                    idx = i
            return idx
        while k:
            t = good()
            nums[t] = nums[t] * m
            k -= 1
        return nums