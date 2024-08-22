class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def array_gcd(arr):
            result = arr[0]
            for i in range(1, len(arr)):
                result = gcd(result, arr[i])
            return result

        check = min(numsDivide)
        gcd = array_gcd(numsDivide)
        nums.sort()
        idx = 0
        while idx < len(nums) and gcd % nums[idx] != 0:
            idx += 1
        return idx if idx != len(nums) else -1
        