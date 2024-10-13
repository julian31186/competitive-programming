class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        c = Counter(nums)
        res = []
        for i in range(len(nums) - k + 1):
            c = Counter()
            take = 0
            acc = 0
            for j in range(i,i + k):
                c[nums[j]] += 1
            a = sorted(c.items(),key=lambda X: (X[1],X[0]), reverse=True)
            for j in range(min(x,len(a))):
                acc += (a[j][0] * a[j][1])
            res.append(acc)
        return res