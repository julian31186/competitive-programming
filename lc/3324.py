class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = []
        for i,c in enumerate(target):
            nxt = "a"
            while True:
                if nxt == c:
                    res.append(target[:i] + nxt)
                    break
                res.append(target[:i] + nxt)
                nxt = chr(ord(nxt) + 1) if ord(nxt) + 1 < 123 else chr(97)
        return res