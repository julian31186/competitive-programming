from collections import defaultdict

def solve(n,k):
    if n // k < 3:
        print("-1")
        return
    
    c = defaultdict(list)
    inv = {}
    idx = 1
    for i in range(1,2 * k + 1, 2):
        c[idx].extend([i,i + 1])
        idx += 1

    idx = 1
    for i in range(2 * k + 1,3 * k + 1):
        c[idx].append(i)
        idx += 1
    
    for i in range(3 * k + 1, n + 1):
        c[k].append(i)

    for k,v in c.items():
        for item in v:
            inv[item] = k

    for i in range(1,n + 1):
        print(inv[i],end=" ")

n,k = map(int, input().split(" "))
solve(n,k)
