class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        h,td = [],sum(damage)
        res = 0
        for i in range(len(damage)):
            heappush(h,(-(damage[i] / (ceil(health[i] / power))),ceil(health[i] / power), damage[i]))
        while h:
            _,hits,d = heappop(h)
            res += td * hits
            td -= d
        return res