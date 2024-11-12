class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        res = 0
        
        start,j,zeros,msb = x,0,[],0
        while start:
            if start & 1: msb = j
            else: zeros.append(j)
            start >>= 1
            j += 1
        
        for i in range(len(zeros)):
            if n & 1:
                x |= ((n & 1) << zeros[i])
            n >>= 1

        return (n << (msb + 1)) | x 