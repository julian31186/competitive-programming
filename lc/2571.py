from collections import deque

class Solution:
    def minOperations(self, n: int) -> int:
        q = deque([(0,n)])
        vis = set([n])
        while q:
            operations,curr = q.popleft()
            if curr.bit_count() == 1: return operations + 1
            if curr == 0: return operations
            for i in range(17):
                if curr + 2**i not in vis:
                    vis.add(curr + 2**i)
                    q.append((operations + 1,curr + 2**i))
                if curr - 2**i not in vis:
                    vis.add(curr - 2**i)
                    q.append((operations + 1,curr - 2**i))
        return -1