class Solution:
    def minTimeToReach(self, mt: List[List[int]]) -> int:

        def valid(i,j):
            return (i >= 0 and i < len(mt) and j >= 0 and j < len(mt[0]))

        dists = defaultdict(lambda: inf)
        dists[(0,0)] = 0
        h = [(0,0,0)]
        
        while h:
            t,i,j = heappop(h)
            
            if dists[(i,j)] < t: continue

            if (i,j) == (len(mt) - 1, len(mt[0]) - 1): 
                return t
                
            for dy,dx in [[-1,0],[1,0],[0,-1],[0,1]]:
                ny,nx = i + dy,j + dx
                if valid(ny,nx) == False:
                    continue
                cost = t + 1 + max(0,mt[ny][nx] - t)
                if cost < dists[(ny,nx)]:
                    dists[(ny,nx)] = cost
                    heapq.heappush(h,(cost, ny, nx))
        
        return -1