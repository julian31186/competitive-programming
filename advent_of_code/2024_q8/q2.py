from collections import deque

f = open("input.txt")

res = set()
a = []

for row in f:
    r = []
    for c in row.strip():
        r.append(c)
    a.append(r)

R,C = len(a),len(a[0])

def is_valid(i,j):
    return (i >= 0 and j >= 0 and i < R and j < C)

def bfs(i,j):

    q = deque([(i,j)])
    vis = set([(i,j)])

    while q:
        y,x = q.popleft()

        if (y,x) != (i,j) and a[y][x] == a[i][j]:
            delta = (y - i, x - j)
            ti,tj = y,x
            while is_valid(ti,tj):
                res.add((ti,tj))
                ti += delta[0]
                tj += delta[1]


        d = [[y + -1,x + -1],[y + -1,x + 0],[y + -1,x + 1],[y + 0,x + -1],[y + 0,x + 1],[y + 1,x + -1],[y + 1,x + 0],[y + 1,x + 1]]

        for ny,nx in d:
            if (ny,nx) not in vis and is_valid(ny,nx):
                vis.add((ny,nx))
                q.append((ny,nx)) 


for i in range(R):
    for j in range(C):
        if a[i][j] != '.':
            bfs(i,j)

print(len(res))