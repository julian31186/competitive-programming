class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def good(i,dir):
            c = nums.copy()
            curr = i
            while True:
                if curr < 0 or curr == len(c): break
                if c[curr] == 0:
                    curr += dir
                elif c[curr] > 0:
                    c[curr] -= 1
                    dir = 1 if dir == -1 else -1
                    curr += dir
            return all(x == 0 for x in c)

        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                res += good(i,1) + good(i,-1)
        return res