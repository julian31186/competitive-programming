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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([(root,-1)])
        while q:
            c,total = defaultdict(int),0
            lvl = []
            for i in range(len(q)):
                curr,parent = q.popleft()
                c[parent] += curr.val
                total += curr.val
                lvl.append((curr,parent))
                if curr.left: q.append((curr.left,curr))
                if curr.right: q.append((curr.right,curr))
            for node,p in lvl:
                node.val = total - c[p]
        return root