# cook your dish here

from collections import Counter

tc = int(input())

def good(a,k):
    c = Counter(a)
    for i in range(len(a)):
        mx = max(c.values())
        if c[k] == mx: return 1
        c[a[i]] -= 1
    return 0

for t in range(tc):
    l = input().split(" ")
    n,k = int(l[0]),int(l[1])
    a = [int(x) for x in input().split(" ")]
    c = Counter(a)
    mx = max(c.values())
    
    if c[k] == mx:
        print(0)
    elif good(a,k) or good(a[::-1],k):
        print(1)
    else:
        print(2)