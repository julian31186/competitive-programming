tc = int(input())

for t in range(tc):
    
    v = set()
    acc = 0
    res = 0
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    LIM = max(a)

    for i in range(len(a)):
        acc += a[i]
        if acc > LIM * 2: break
        v.add(a[i])
        div = acc / 2
        if div.is_integer() and div in v:
            res += 1
    
    print(res)