class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,w):
        curr = self.root
        for c in w:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        tri = Trie()
        for w in dictionary:
            tri.insert(w)

        @cache
        def dp(idx):
            if idx == len(s): return 0
            skip = dp(idx + 1)
            take = 0
            root = tri.root
            for i in range(idx,len(s)):
                if s[i] in root.children:
                    root = root.children[s[i]]
                    if root.end:
                        take = max(take, (i - idx + 1) + dp(i + 1))
                else:
                    break
            return max(take,skip)

        return len(s) - dp(0)