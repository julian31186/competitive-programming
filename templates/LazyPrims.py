import heapq
import math

'''
TC: O(ElogE)
SC: E

(E can be at most V^2 in a fully connected graph)
(so ElogE becomes ElogV^2 == ElogV because of log rules)

'''

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
        pq = [(0, self.start,self.start)]
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