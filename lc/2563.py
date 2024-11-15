from sortedcontainers import SortedList
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sl,res = SortedList(),0
        for x in nums:
            if sl: res += sl.bisect_right(upper - x) - sl.bisect_left(lower - x)
            sl.add(x)
        return res