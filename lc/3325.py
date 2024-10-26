class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        res = 0
        l = 0
        c = defaultdict(int)
        for i in range(len(s)):
            c[s[i]] += 1
            while any(v >= k for v in c.values()):
                c[s[l]] -= 1
                l += 1
            res += l
        return res