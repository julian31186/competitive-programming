class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        
        a = []
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            a.append(acc)

        @cache
        def dp(i,kleft,can_extend):
            if i + (kleft * m) > len(a):
                return -inf
            if i == len(a): 
                return 0 if kleft == 0 else -inf
            res = dp(i + 1,kleft,False)
            if can_extend:
                res = max(res, nums[i] + dp(i + 1,kleft,True))
            if kleft:
                res = max(res,(a[i + m - 1] - (a[i - 1] if i - 1 >= 0 else 0)) + dp(i + m,kleft - 1,True))
            return res
            
        x = dp(0,k,False)
        dp.cache_clear()
        return x