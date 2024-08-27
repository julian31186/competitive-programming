class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        c = defaultdict(int)
        curr = defaultdict(int)
        currq = deque()
        l = 0
        for r in range(len(s)):
            curr[s[r]] += 1
            currq.append(s[r])
            while ((r - l + 1) > minSize) or (len(curr) > maxLetters):
                currq.popleft()
                curr[s[l]] -= 1
                if curr[s[l]] == 0: del curr[s[l]]
                l += 1
            c["".join(currq)] += 1 if r - l + 1 == minSize else 0
        return max(c.values())