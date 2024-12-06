from collections import defaultdict,deque

f = open("input.txt")

res = 0
b = defaultdict(set)
adj = defaultdict(list)
rules = []

for i,row in enumerate(f):
    if row == "\n": break
    u,v = [int(x) for x in row.split("|")]
    rules.append((u,v))
    b[u].add(v)
    adj[u].append(v)


for row in f:
    a,f = [int(x) for x in row.split(",")],True
    for i in range(len(a)):
        for j in range(i + 1,len(a)):
            if a[i] in b[a[j]]:
                f = False
                break
        
        if not f: break

    if not f:
        indeg = defaultdict(int)
        for u,v in rules:
            if u in a and v in a:
                indeg[v] += 1

        q = deque()
        fix = []
        for x in a:
            if indeg[x] == 0:
                q.append(x)
        
        while q:
            curr = q.popleft()
            fix.append(curr)
            for nei in adj[curr]:
                indeg[nei] -= 1
                if indeg[nei] == 0: q.append(nei)

        res += fix[len(fix) // 2]

print(res)