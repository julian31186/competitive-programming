class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        a = []
        def dfs(root):
            if not root: return
            x = bfs(root)
            if x[0]: a.append(x[1]) 
            dfs(root.left)
            dfs(root.right)
        
        def bfs(root):
            q = deque([root])
            l = []
            lvl = 0
            count = 0
            while q:
                sz = len(q)
                for i in range(sz):
                    curr = q.popleft()
                    count += 1
                    if (curr.left == None and curr.right == None): l.append(lvl)
                    elif (curr.left and curr.right): 
                        q.append(curr.left)
                        q.append(curr.right)
                    else: 
                        return [False,-1]
                lvl += 1
            
            return [len(Counter(l)) == 1,count]
        
        dfs(root)
        a.sort(reverse=True)
        return a[k - 1] if k - 1 < len(a) else -1