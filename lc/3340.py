class Solution:
    def isBalanced(self, num: str) -> bool:
        o,e = 0,0
        for i in range(len(num)):
            if i % 2 == 0: e += int(num[i])
            else: o += int(num[i])
        return e == o