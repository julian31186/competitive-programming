import math
from operator import xor

class SparseTable():
    '''
    Time Complexity: 
        O(nlogn) build
        O(1) query
    
    Space Complexity:
        O(nlogn)
    '''
    def __init__(self,arr,fn):
        '''
        Note:
            fn must be idempotent (fn(x,x) == x)
            - min()
            - max()
            - gcd()
            - lcm()
            - AND
            - OR
        ''' 
        self.n = len(arr)
        self.m = math.floor(math.log2(self.n)) + 1
        self.fn = fn
        self.arr = arr
        self.table = [[0 for _ in range(self.m)] for _ in range(self.n)]

    def build(self):
        for i in range(self.n):
            self.table[i][0] = self.arr[i]
        for j in range(1, self.m):
            for i in range(self.n - (1 << j) + 1):
                #                             Left Half                       Right Half
                self.table[i][j] = self.fn(self.table[i][j - 1], self.table[i + (1 << (j - 1))][j - 1])                

    def query(self,l,r):
        k = math.floor(math.log2(r - l + 1))
        return self.fn(
            self.table[l][k],
            self.table[r - (1 << k) + 1][k]
        )

n, q = map(int, input().split())
arr = list(map(int, input().split()))

res = []

st = SparseTable(arr,min)
st.build()

for _ in range(q):
    l,r = map(int, input().split())
    print(st.query(l - 1,r - 1))
