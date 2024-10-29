class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        @cache
        def dp(i,g1,g2):
            if i == len(nums): return 1 if g1 == g2 != -1 else 0
            return (dp(i + 1,nums[i] if g1 == -1 else gcd(g1,nums[i]),g2) % MOD + dp(i + 1,g1,nums[i] if g2 == -1 else gcd(g2,nums[i])) % MOD + dp(i + 1,g1,g2) % MOD) % MOD
        x = dp(0,-1,-1)
        dp.cache_clear()
        return x