class TrieNode():
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,str) -> None:
        curr = self.root
        for c in str:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr.children[c].count += 1
            curr = curr.children[c]

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        tri,res = Trie(),[]
        for w in words:
            tri.insert(w)
        for w in words:
            root,cnt = tri.root,0
            for c in w:
                cnt += root.children[c].count
                root = root.children[c]
            res.append(cnt)
        return res