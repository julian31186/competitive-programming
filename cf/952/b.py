tc = int(input())

for t in range(tc):
    n = int(input())
    res = [0,0]
    for i in range(2,n + 1):
        acc = 0
        x = i
        while x <= n:
            acc += x
            x += i
        if acc > res[0]:
            res[0] = acc
            res[1] = i

    print(res[1])
