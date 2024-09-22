class Solution:
    def validSubstringCount(self, w1: str, w2: str) -> int:
        w2 = Counter(w2)

        c = Counter()
        l = 0
        res = 0
        for r in range(len(w1)):
            c[w1[r]] += 1
            while c >= w2:
                c[w1[l]] -= 1
                l += 1
            res += l
        
        return res