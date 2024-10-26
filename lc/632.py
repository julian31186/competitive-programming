class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        a = []
        for i in range(len(nums)):
            for x in nums[i]:
                a.append((x,i))
        a.sort()
        c = defaultdict(int)
        l = 0
        res = [0,10**6]
        for r in range(len(a)):
            c[a[r][1]] += 1
            while len(c) == k:
                if (res[1] - res[0]) > (a[r][0] - a[l][0]):
                    res[0] = a[l][0]
                    res[1] = a[r][0]
                c[a[l][1]] -= 1
                if c[a[l][1]] == 0: del c[a[l][1]]
                l += 1
        return res