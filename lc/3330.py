class Solution:
    def possibleStringCount(self, word: str) -> int:
        res,r = 1,0
        while r < len(word):
            c = 0
            while r < len(word) - 1 and word[r] == word[r + 1]:
                c += 1
                r += 1
            res += c
            r += 1
        return res