class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        l,res,cnt = 0,inf,[0] * 32

        def update(x,delta):
            j = 0
            while x:
                if x & 1:
                    cnt[j] += delta
                j += 1
                x >>= 1

        def good():
            acc = 0
            for i in range(len(cnt)):
                if cnt[i] > 0: acc += 2**(i)
            return acc >= k


        for r in range(len(nums)):
            update(nums[r],1)
            while l <= r and good():
                update(nums[l], -1)
                res = min(res,r - l + 1)
                l += 1

        return res if res != inf else -1