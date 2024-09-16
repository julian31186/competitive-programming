class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        def lbs(x):
            l,r = 0,len(nums) - 1
            while l < r:
                mid = (r + l) // 2
                if nums[mid] >= x: r = mid
                elif nums[mid] < x: l = mid + 1
            return r if nums[r] == x else -1
        def ubs(x): 
            l,r,res = 0,len(nums) - 1,-1
            while l <= r:
                mid = (r + l) // 2
                if nums[mid] <= x:
                    res = mid if nums[mid] == x else res
                    l = mid + 1
                elif nums[mid] > x: r = mid - 1
            return res
        return [lbs(target),ubs(target)]