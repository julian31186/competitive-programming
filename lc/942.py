class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        res = []
        h,l = n,0
        for i in range(len(s)):
            if s[i] == "I":
                res.append(l)
                l += 1
            else:
                res.append(h)
                h -= 1
        return res + [l] if s[-1] == "D" else res + [h]