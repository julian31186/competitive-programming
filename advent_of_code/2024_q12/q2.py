from collections import deque

f = open("input.txt")
res = 0
a = []

for row in f:
    r = []
    for c in row.strip():
        r.append(c)
    a.append(r)

R,C = len(a),len(a[0])
vis = set()

def bfs(i,j,c):
    s,area = set(),0
    q = deque([(i,j)])
    while q:
        y, x = q.popleft()
        area += 1
        for ny,nx in [[y + -1, x + 0],[y + 1, x + 0],[y + 0, x + -1],[y + 0, x + 1]]:
            if not (ny >= 0 and nx >= 0 and ny < R and nx < C):
                if ny < 0 or ny >= R:
                    s.add((ny,'R'))
                if nx < 0 or nx >= C:
                    s.add((nx,'C'))
                continue
            if (ny,nx) in vis or a[ny][nx] != c:
                if abs(ny - y) == 1 and a[ny][nx] != a[y][x]:
                    s.add((ny,'R',0 if y < ny else 1))
                if abs(nx - x) == 1 and a[ny][nx] != a[y][x]:
                    s.add((nx,'C',0 if y < ny else 1))
                continue
            if a[ny][nx] == c:
                vis.add((ny,nx))
                q.append((ny,nx))
    
    print(c,len(s),area,s)
    return len(s) * area


for i in range(R):
    for j in range(C):
        if (i,j) not in vis:
            vis.add((i,j))
            res += bfs(i,j,a[i][j])

print(res)