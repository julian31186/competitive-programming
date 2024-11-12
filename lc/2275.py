class Solution:
    def largestCombination(self, c: List[int]) -> int:
        cnt = [0] * 32
        for i,x in enumerate(c):
            j = 0
            while x:
                if x & 1: cnt[j] = 1 + cnt[j] 
                j += 1
                x >>= 1
        return max(cnt)