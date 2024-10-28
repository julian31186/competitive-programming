'''
TC: O(nlogn)
SC: O(n)

Remember we can prune the streak if its sqrt() exists in the set. If thats the case then, at some
point we will get to it in the inner while, no point to check it more than once. 

Although since n <= 10^5, the repeated work is fine here since the longest streak can be of at most
size 16
'''
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        res,v = -1,set(nums)
        for i,num in enumerate(nums):
            if sqrt(num) in v: continue
            cnt,t = 1,num
            while t * t in v:
                cnt += 1
                t *= t
            if cnt > 1: res = max(res,cnt)
        return res