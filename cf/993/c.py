tc = int(input())

for t in range(tc):
    m,a,b,c = [int(x) for x in input().split(" ")]
    res = 0
    extra = 0
    res += min(m,a)
    extra += max(0,m - a)
    res += min(m,b)
    extra += max(0,m - b)
    res += min(extra,c)
    print(res)
