class TrieNode():
    def __init__(self):
        self.children = {}
        self.last = False
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    def insert(self,w):
        root = self.root
        for c in w:
            if c in root.children:
                root = root.children[c]
            else:
                root.children[c] = TrieNode()
                root = root.children[c]
        root.last = True
        return
    def find(self,w):
        root = self.root
        for i,c in enumerate(w):
            if c not in root.children or root.last == True: return i
            else: root = root.children[c]
        return len(w)

class Solution:
    def removeSubfolders(self, f: List[str]) -> List[str]:
        g,tri,res = [[hash(x) for x in path.split("/")] for path in f],Trie(),[]
        for p in g: tri.insert(p)
        for i,p in enumerate(g):
            if tri.find(p) == len(p): res.append(i)
        return [f[i] for i in res]