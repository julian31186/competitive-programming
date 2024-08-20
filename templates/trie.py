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
