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
    perim,area = 0,0
    q = deque([(i,j)])
    while q:
        y, x = q.popleft()
        area += 1
        for ny,nx in [[y + -1, x + 0],[y + 1, x + 0],[y + 0, x + -1],[y + 0, x + 1]]:
            if not (ny >= 0 and nx >= 0 and ny < R and nx < C):
                perim += 1    
                continue
            if (ny,nx) in vis or a[ny][nx] != c:
                perim += 1 if a[ny][nx] != a[y][x] else 0
                continue
            if a[ny][nx] == c:
                vis.add((ny,nx))
                q.append((ny,nx))
    
    print(c,perim,area)
    return perim * area


for i in range(R):
    for j in range(C):
        if (i,j) not in vis:
            vis.add((i,j))
            res += bfs(i,j,a[i][j])

print(res)