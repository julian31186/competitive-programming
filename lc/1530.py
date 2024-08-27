class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root: return []
            if not root.left and not root.right: return [0]
            l = dfs(root.left)
            r = dfs(root.right)
            for i in range(len(l)): l[i] += 1
            for i in range(len(r)): r[i] += 1
            if len(l) + len(r) > 1:
                for i in range(len(l)):
                    for j in range(len(r)):
                        if l[i] + r[j] <= distance:
                            res += 1         
            return l + r
        dfs(root)
        return res