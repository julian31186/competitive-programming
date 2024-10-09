class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = int(bin(nums[i])[2:])
        def cmp(a,b):
            a,b = str(a),str(b)
            if int(a + b) > int(b + a): return -1
            elif int(a + b) < int(b + a): return 1
            else: return 0
        nums.sort(key=cmp_to_key(cmp))
        return int("".join([str(x) for x in nums]),2)