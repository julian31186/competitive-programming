class Solution:
    '''
    Modification from my original solution which did AC, however I checked all possible combinations of substrings (and checked for validity at the base case) 
    which runs 10x slower than with this optimization. In this new approach (inspired from larrys server), we do the work of checking if its valid on the go 
    which effectively prunes the decision tree and saves a ton of time.

    sup matt ;)

    TC: O(n * 2^n)?
    SC: O(n) as the stack can grow to O(n) at max when we pick each individual character as its own substring
    '''
    def maxUniqueSplit(self, s: str) -> int:
        def go(idx,arr):
            if idx == len(s): return len(arr)
            res = 0
            for i in range(idx,len(s)):
                if s[idx:i + 1] not in arr:
                    arr.append(s[idx:i + 1])
                    res = max(res, go(i + 1,arr))
                    arr.pop()
            return res
        return go(0,[])