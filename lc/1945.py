class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = list(s)
        for i in range(len(s)):
            s[i] = (ord(s[i]) - ord('a')) + 1
        s = "".join([str(x) for x in s])
        while k:
            acc = sum(int(x) for x in s)
            s = str(acc)
            k -= 1
        return int(s)