class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], sp: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for (u,v),c in zip(edges,sp):
            adj[u].append((c,v))
            adj[v].append((c,u))
        heap,dists = [(-1,start_node)],{}
        for i in range(n): dists[i] = inf
        while heap:
            prob, node = heapq.heappop(heap)
            if node == end_node: return -prob
            if dists[node] < prob: continue
            for cost,nei in adj[node]:
                new_cost = prob * cost
                if new_cost < dists[nei]:
                    dists[nei] = new_cost
                    heapq.heappush(heap,(new_cost, nei))
        return 0