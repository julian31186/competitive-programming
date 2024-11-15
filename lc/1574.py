class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        l,r,c,res = 0,len(arr) - 1,0,0
        a = [[0,0] for i in range(len(arr))]

        for i in range(len(arr) -1, -1, -1):
            if i == len(arr) - 1 or arr[i] > arr[i + 1]: c = 1
            else: c += 1
            a[i][1] = c
        
        for i in range(0,len(arr)):
            if i == 0 or arr[i] < arr[i - 1]: c = 1
            else: c += 1
            a[i][0] = c

        def good(k):
            for r in range(k - 1,len(a)):
                l,el = 0 if r == k - 1 else a[r - k][0],0 if r == k - 1 else arr[r - k]
                r,er = 0 if r == len(a) - 1 else a[r + 1][1],inf if r == len(a) - 1 else arr[r + 1]
                if l + r == len(a) - k and el <= er: return True
            return False
                 
        while l <= r:
            mid = (r + l) // 2
            if good(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res