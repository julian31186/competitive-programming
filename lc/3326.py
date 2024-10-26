class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0

        def gcd_(x,y):
            for i in range(2,ceil(sqrt(x)) + 1):
                if x % i == 0:                    
                    return i
            return -1
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]: continue
            x = gcd_(nums[i],nums[i + 1])
            if x == -1 or x > nums[i + 1]: return -1
            else:
                nums[i] = x
                res += 1
        return res