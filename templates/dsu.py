class DSU:
    def __init__(self,n):
        self.arr = [-1] * n

    def union(self,a,b):
        par_a = a
        while self.arr[par_a] >= 0:
            par_a = self.arr[par_a]
        par_b = b
        while self.arr[par_b] >= 0:
            par_b = self.arr[par_b]
        
        if par_a == par_b: return

        if abs(self.arr[par_a]) > abs(self.arr[par_b]):
            self.arr[par_a] += self.arr[par_b]
            self.arr[par_b] = par_a
        else:
            self.arr[par_b] += self.arr[par_a]
            self.arr[par_a] = par_b
    
    def find(self,x):
        parent = x
        while self.arr[parent] >= 0:
            parent = self.arr[parent]
        
        compress = x
        while self.arr[compress] >= 0:
            temp = self.arr[compress]
            self.arr[compress] = parent
            compress = temp
        return parent 
    
    def count(self):
        cc = 0
        for x in self.arr:
            if x < 0: cc += 1
        return cc