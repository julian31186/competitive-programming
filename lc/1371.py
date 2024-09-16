class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        cache = { 'a' : 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4 }
        c = { 0 : -1 }
        acc = 0
        res = 0
        for i,char in enumerate(s):
            if char in cache:
                acc ^= (1 << cache[char])
                if acc not in c: c[acc] = i
            res = max(res,i - c[acc])
        return res