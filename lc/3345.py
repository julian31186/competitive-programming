class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i = n
        while True:
            acc = 1
            for c in str(i):
                acc *= int(c)
            if acc % t == 0: return i
            i += 1