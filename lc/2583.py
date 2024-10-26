# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Maintain min heap of size k to keep track of kth largest. This is optimal in cases where k << n,
otherwise it is similar to never removing from the heap until the end (nlogn)

TC: (O(n * log(k))
SC: O(n) since we maintain a heap of size k and k can equal n 
'''

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q,min_heap = deque([root]),[]
        while q:
            lvl_sum = 0
            for i in range(len(q)):
                curr = q.popleft()
                lvl_sum += curr.val
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            if len(min_heap) < k: heappush(min_heap,lvl_sum)
            elif lvl_sum > min_heap[0]: heappushpop(min_heap,lvl_sum)
        return -1 if len(min_heap) < k else min_heap[0]