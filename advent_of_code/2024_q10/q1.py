from collections import deque

f = open("input.txt")

a = []
res = 0

for row in f:
    r = []
    for c in row.strip():
        r.append(c)
    a.append(r)

R,C = len(a),len(a[0])

def bfs(i,j):
    cnt = 0
    vis = set([(i,j)])
    q = deque([(0,i,j)])

    while q:
        step, y, x = q.popleft()
        if a[y][x] =='9':
            cnt += 1
            continue
        for ny,nx in [[y + -1, x + 0],[y + 1, x + 0],[y + 0, x + -1],[y + 0, x + 1]]:
            if not (ny >= 0 and nx >= 0 and ny < R and nx < C) or (ny,nx) in vis: continue
            if a[ny][nx] == str(step + 1):
                vis.add((ny,nx))
                q.append((step + 1,ny,nx))
    return cnt


for i in range(R):
    for j in range(C):
        if a[i][j] == '0':
            res += bfs(i,j)

print(res)