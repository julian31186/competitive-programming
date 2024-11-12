class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        acc = list(accumulate(nums,operator.xor))
        for i in range(len(acc) - 1, -1, -1):
            j,t,query_ans = 0,acc[i],0
            while j < maximumBit:
                if t & 1 == 0: query_ans |= (1 << j)
                j += 1
                t >>= 1
            acc[i] = query_ans
        return acc[::-1]