class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        for i in range(len(times)):
            times[i].append(i)
        times.sort(key = lambda x: x[0])
        seats,end = list(range(len(times))),[]
        for s,e,idx in times:
            while end and end[0][0] <= s:
                _,chair = heappop(end)
                heappush(seats,chair)
            if idx == targetFriend:
                return heappop(seats)
            heappush(end,(e,heappop(seats)))
        return -1