# cook your dish here

from collections import defaultdict

tc = int(input())

for t in range(tc):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    f = True
    c = defaultdict(int)
    
    for i,n in enumerate(a):
        c[n] = [i,n.bit_count()]
    
    for i in range(len(a)):
        if a[i] == i + 1: continue
        if c[a[i]][1] != c[i + 1][1]:
            f = False
            print("No")
            break
        else:
            curr_idx,need_to_go = i,c[i + 1][0]
            c[a[i]][0] = need_to_go
            c[i + 1][0] = i
            a[i],a[need_to_go] = a[need_to_go],a[i]
    
    if f: print("Yes")