class TrieNode():
    def __init__(self):
        self.children = {}
        self.last = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,str) -> None:
        curr = self.root
        for c in str:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.last = True
            
    def find(self,str) -> int:
        curr = self.root
        for i,c in enumerate(str):
            if c in curr.children:
                curr = curr.children[c]
            else:
                return i
        return len(str)

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        tri = Trie()
        for w in words:
            tri.insert(w)
        @cache
        def dfs(idx):
            if idx == len(target):
                return 0
            res = inf
            acc = tri.root
            for i in range(idx,len(target)):
                if target[i] in acc.children:
                    acc = acc.children[target[i]]
                    res = min(res,1 + dfs(i + 1))
                else:
                    break

            return res
        x = dfs(0)
        
        return x if x != inf else -1