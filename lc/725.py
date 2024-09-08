# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        sz,trav,res = 0,head,[]
        while trav:
            sz += 1
            trav = trav.next
        q,r = divmod(sz, k)
        j,trav,prev = 0,head,None
        for i in range(r):
            if trav:
                res.append(trav)
                while trav and j < q + 1:
                    prev = trav
                    trav = trav.next
                    j += 1
                if prev: prev.next = None
                prev = None
                j = 0
        i = 0
        while trav:
            if i % q == 0:
                if prev: prev.next = None
                res.append(trav)
            prev = trav
            trav = trav.next
            i += 1
        return res + [None] * (k - len(res))