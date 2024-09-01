from sortedcontainers import SortedList
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        sl = SortedList()
        res = []
        for u,v in queries:
            sl.add(abs(u) + abs(v))
            if len(sl) >= k: res.append(sl[k - 1])
            else: res.append(-1)
        return res