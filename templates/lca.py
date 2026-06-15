import math

# (Written By Claude)

class LCA:
    """
    Lowest Common Ancestor via binary lifting.

    Build: O(n log n) time, O(n log n) space.
    Query: O(log n) time per call.
    """

    def __init__(self, n, adj):
        # O(n log n) — allocates the n x (l+1) ancestor table.
        self.n = n
        self.adj = adj
        self.l = max(1, math.ceil(math.log2(n))) if n > 1 else 1
        self.tin = [0] * n
        self.tout = [0] * n
        self.up = [[0] * (self.l + 1) for _ in range(n)]
        self._built = False

    def build(self, root):
        # O(n log n) — single DFS visits each node once (O(n)),
        # and each visit fills l = O(log n) binary-lifting entries.
        l = self.l
        tin, tout, up, adj = self.tin, self.tout, self.up, self.adj
        timer = 0

        # Iterative DFS — avoids Python's recursion limit on large n
        stack = [(root, root, False)]
        while stack:
            v, p, exiting = stack.pop()
            if exiting:
                timer += 1
                tout[v] = timer
            else:
                timer += 1
                tin[v] = timer
                up[v][0] = p
                for i in range(1, l + 1):  # O(log n) per node
                    up[v][i] = up[up[v][i - 1]][i - 1]
                stack.append((v, p, True))
                for u in adj[v]:
                    if u != p:
                        stack.append((u, v, False))

        self._built = True
        return self

    def is_ancestor(self, u, v):
        # O(1) — two timestamp comparisons.
        return self.tin[u] <= self.tin[v] and self.tout[u] >= self.tout[v]

    def query(self, u, v):
        # O(log n) — climbs the binary-lifting table at most l = O(log n) times.
        if not self._built:
            raise RuntimeError("call build(root) before query()")
        if self.is_ancestor(u, v):
            return u
        if self.is_ancestor(v, u):
            return v
        for i in range(self.l, -1, -1):  # O(log n) iterations
            if not self.is_ancestor(self.up[u][i], v):
                u = self.up[u][i]
        return self.up[u][0]
