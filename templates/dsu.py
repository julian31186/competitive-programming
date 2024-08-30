class DSU:
    def __init__(self,n):
        self.p = [-1] * n

    def union(self,a,b):
        i,j = self.find(a),self.find(b)
        if i == j: return
        if self.p[i] > self.p[j]: i,j = j,i
        self.p[i] += self.p[j]
        self.p[j] = i 
    
    def find(self,i):
        if self.p[i] < 0: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    
    def count(self):
        cc = 0
        for x in self.p:
            if x < 0: cc += 1
        return cc