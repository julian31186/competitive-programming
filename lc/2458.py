# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        res,b,bb,l = [],defaultdict(lambda: [(0,0),(0,0)]),defaultdict(int),defaultdict(int)

        def dfs(root):
            if not root: return 0
            dfs(root.left)
            dfs(root.right)
            bb[root.val] = 1 + max(bb[root.left.val] if root.left else 0,bb[root.right.val] if root.right else 0)
            return bb[root.val]
        
        def bfs(root):
            q = deque([root])
            lvl = 0
            while q:
                for i in range(len(q)):
                    curr = q.popleft()
                    if bb[curr.val] > b[lvl][0][0]:
                        b[lvl][1] = b[lvl][0]
                        b[lvl][0] = (bb[curr.val],curr.val)
                    elif bb[curr.val] > b[lvl][1][0]:
                        b[lvl][1] = (bb[curr.val],curr.val)
                    l[curr.val] = lvl
                    if curr.left: q.append(curr.left)
                    if curr.right: q.append(curr.right)
                lvl += 1
            return

        dfs(root)
        bfs(root)
        for v in queries:
            res.append((l[v] + (b[l[v]][0][0] if v != b[l[v]][0][1] else b[l[v]][1][0])) - 1)
        return res