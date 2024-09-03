class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k -= sum(chalk) * (k // sum(chalk))
        i = 0
        while k:
            if k < chalk[i]: return i
            k -= chalk[i]
            i += 1
        return i