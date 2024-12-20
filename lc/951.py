# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
TC: O(n)
SC: O(n)
'''
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(r1,r2):
            if r1 == None and r2 == None: return True
            if r1 == None or r2 == None: return False
            if r1.val != r2.val: return False
            return (
                (dfs(r1.left,r2.left) and dfs(r1.right,r2.right)) or
                (dfs(r1.right,r2.left) and dfs(r1.left,r2.right))
            )
        return dfs(root1,root2)