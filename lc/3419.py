class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        
        # Bin Search
        def good(maxw):
            adj = defaultdict(list)
            vis = set()
            for u,v,c in edges:
                if c <= maxw:
                    adj[v].append((c,u))
            
            q = deque([0])
            vis = set([0])
            while q:
                curr = q.popleft()
                for cost,nei in adj[curr]:
                    if nei not in vis:
                        vis.add(nei)
                        q.append(nei)
            
            return len(vis) == n
        
        res,l,r = -1,1,(10**6) + 1
        while l <= r:
            mid = (r + l) // 2
            if good(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res

'''

import heapq
import math

TC: O(ElogE)
SC: E

(E can be at most V^2 in a fully connected graph)
(so ElogE becomes ElogV^2 == ElogV because of log rules)


Prims sol, actually unsure why this works in retrospect since this is a directed graph and prims should only
work on undirected

class LazyPrims:
    
    def __init__(self, n, adj, start):
        
        # Dict of -> Key : (weight, neighbor)
        self.adj = adj
        self.start = start
        self.n = n

        self._edges = []
        self._cost = -math.inf
        self._vis = set()
    
    def buildMST(self):
        pq = [(0, self.start, self.start)]
        cost = 0

        while pq:
            cost_to_curr_node,from_,to_ = heapq.heappop(pq)
            
            # Stale node (already added to MST with better path)
            if to_ in self._vis: continue

            if from_ != to_: 
                self._edges.append((from_,to_,cost_to_curr_node))

            self._vis.add(to_)

            cost += cost_to_curr_node

            for edge_weight, nei in self.adj[to_]:
                if nei not in self._vis:
                    heapq.heappush(pq,(edge_weight, to_, nei))
        
        # We have not added n nodes to the graph meaning the graph is disconnected
        if len(self._vis) != self.n:
            return

        self._cost = cost
        return

    def getMSTCost(self):
        # Returns the cost of the MST, or -inf if we cannot build an MST (graph is disconnected)
        return self._cost

    def getMSTEdges(self):
        return self._edges
        
class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        adj = defaultdict(list)
        for u,v,c in edges:
            adj[v].append((c,u))

        vis = set()
        def dfs(root):
            if root in vis: return
            vis.add(root)
            for _,nei in adj[root]:
                dfs(nei)
        dfs(0)
        if len(vis) != n: return -1
            
        lp = LazyPrims(n,adj,0)
        lp.buildMST()
        return max([x[2] for x in lp.getMSTEdges()])
        
'''
