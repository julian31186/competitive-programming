class Solution:
    def maximumTotalSum(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        last = inf
        res = 0
        for i in range(len(arr)):
            if last <= arr[i]: arr[i] = last - 1
            last = arr[i]
            if last == 0: return -1
            res += last
        return res