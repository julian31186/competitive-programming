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
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        res,tri,arr1,arr2 = 0,Trie(),list(map(str, arr1)),list(map(str, arr2))
        for w in arr2: tri.insert(w)
        return max([tri.find(w) for w in arr1])