'''
Given a list of edges [u,v], build an adjacency list, then use TreeHelper for
depth / distance / diameter queries on an (unweighted) tree.

TreeHelper extends LCA (binary lifting), so it inherits build()/query().

*Roots the tree at the node passed to build()
'''

from collections import deque

from lca import LCA

# (Written By Claude)

class TreeHelper(LCA):
    """
    Tree utilities on top of LCA.

    build:    O(n log n)   (LCA preprocessing + one O(n) pass for depths)
    depth:    O(1)
    distance: O(log n)     (dominated by the LCA query)
    diameter: O(n)         (double BFS, computed once and cached)
    """

    def __init__(self, n, adj):
        super().__init__(n, adj)
        self.depth = [0] * n
        self._diameter = None

    def build(self, root):
        # O(n log n) — run LCA preprocessing, then fill depths in O(n).
        super().build(root)
        self.root = root
        self._fill_depths(root)
        self._diameter = None  # invalidate cache on rebuild
        return self

    def get_depth(self, node):
        # O(1) — depth (number of edges from the root).
        if not self._built:
            raise RuntimeError("call build(root) before get_depth()")
        return self.depth[node]

    def distance(self, a, b):
        # O(log n) — edges on the path a..b = depth(a) + depth(b) - 2*depth(lca).
        return self.depth[a] + self.depth[b] - 2 * self.depth[self.query(a, b)]

    def diameter(self):
        # O(n) — longest path (in edges) via double BFS; cached after first call.
        if self._diameter is None:
            # BFS from any node finds one endpoint of a diameter,
            # BFS from that endpoint gives the diameter length.
            u, _ = self._bfs_farthest(self.root)
            _, dist = self._bfs_farthest(u)
            self._diameter = dist
        return self._diameter

    def _bfs_farthest(self, src):
        # O(n) — returns (farthest_node, its_distance) from src.
        adj = self.adj
        dist = [-1] * self.n
        dist[src] = 0
        dq = deque([src])
        far_node, far_dist = src, 0
        while dq:
            v = dq.popleft()
            if dist[v] > far_dist:
                far_dist, far_node = dist[v], v
            for u in adj[v]:
                if dist[u] == -1:
                    dist[u] = dist[v] + 1
                    dq.append(u)
        return far_node, far_dist

    def _fill_depths(self, root):
        # O(n) — BFS from the root; depth[root] = 0.
        depth, adj = self.depth, self.adj
        depth[root] = 0
        visited = [False] * self.n
        visited[root] = True
        dq = deque([root])
        while dq:
            v = dq.popleft()
            for u in adj[v]:
                if not visited[u]:
                    visited[u] = True
                    depth[u] = depth[v] + 1
                    dq.append(u)
