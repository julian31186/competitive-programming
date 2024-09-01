class Solution:
    def checkTwoChessboards(self, c1: str, c2: str) -> bool:
        col1,row1 = ord(c1[0]) - ord('a'),int(c1[1])
        col2,row2 = ord(c2[0]) - ord('a'),int(c2[1])
        c1,c2 = defaultdict(int),defaultdict(int)
        c1[col1 % 2 == 0] += 1
        c1[row1 % 2 == 0] += 1

        c2[col2 % 2 == 0] += 1
        c2[row2 % 2 == 0] += 1

        return len(c1) == len(c2)