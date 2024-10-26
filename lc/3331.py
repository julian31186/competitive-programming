class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        res = [-1] * len(parent)
        
        def create_adj():
            adj = defaultdict(list)
            for child,p in enumerate(parent):
                if child != -1:
                    adj[p].append((child,s[child]))
            return adj

        def dfs1(root,c,a):
            if c in a: parent[root] = a[c]
            a[c] = root
            for child,schild in adj[root]:
                dfs1(child,schild,a.copy())        

        def dfs2(root):
            sz = 1
            for child,_ in adj[root]:
                sz += dfs2(child)
            res[root] = sz
            return sz

        adj = create_adj()
        dfs1(0,s[0],defaultdict(int))
        adj = create_adj()
        dfs2(0)
        return res