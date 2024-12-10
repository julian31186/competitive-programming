from collections import deque
from functools import cache

f = open("input.txt")

a = []
res = 0

for row in f:
    r = []
    for c in row.strip():
        r.append(c)
    a.append(r)

R,C = len(a),len(a[0])

def valid(i,j):
    return (i >= 0 and j >= 0 and i < R and j < C)

@cache
def dfs(i,j):
    if not valid(i,j): return 0
    if a[i][j] == '9': return 1
    y,x,cnt,step = i,j,0,int(a[i][j])
    for ny,nx in [[y + -1, x + 0],[y + 1, x + 0],[y + 0, x + -1],[y + 0, x + 1]]:
        if valid(ny,nx) and a[ny][nx] == str(step + 1):
            cnt += dfs(ny,nx)
    return cnt
    

for i in range(R):
    for j in range(C):
        if a[i][j] == '0':
            res += dfs(i,j)

print(res)