class Solution:
    def construct2DArray(self, og: List[int], m: int, n: int) -> List[List[int]]:
        if len(og) != n * m: return []
        res = []
        i = 0
        while i < len(og):
            curr = []
            for j in range(i,i + n):
                curr.append(og[j])
            i += n
            res.append(curr)
        return res