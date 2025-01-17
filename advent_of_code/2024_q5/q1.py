from collections import defaultdict,deque

f = open("input.txt")

res = 0
b = defaultdict(set)

for i,row in enumerate(f):
    if row == "\n": break
    u,v = [int(x) for x in row.split("|")]
    b[u].add(v)

for row in f:
    a,f = [int(x) for x in row.split(",")],True
    for i in range(len(a)):
        for j in range(i + 1,len(a)):
            if a[i] in b[a[j]]:
                f = False
                break
        if not f: break
    
    if f:
        res += a[len(a) // 2]
    

print(res)