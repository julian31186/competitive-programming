class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        res = set([x for x in range(n)])
        i = set()
        vis = set()
        adj = defaultdict(list)
        for u,v in invocations:
            adj[u].append(v)
        def dfs(root):
            if root in vis: return
            vis.add(root)
            i.add(root)
            for nei in adj[root]:
                dfs(nei)
        dfs(k)
        for u,v in invocations:
            if u not in i and v in i: 
                i.clear()
                break
        return res - i