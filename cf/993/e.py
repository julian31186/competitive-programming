tc = int(input())

def lbs(l1,r1,l2,r2,n,powers):
    res = -1
    while l1 <= r1:
        mid = l1 + ((r1 - l1) // 2)
        val = (mid * (powers[n]))
        if l2 <= val <= r2:
            res = mid
            r1 = mid - 1
        elif val > r2:
            r1 = mid - 1
        else:
            l1 = mid + 1
    return res

def ubs(l1,r1,l2,r2,n,powers):
    res = -1
    while l1 <= r1:
        mid = l1 + ((r1 - l1) // 2)
        val = (mid * (powers[n]))
        if l2 <= val <= r2:
            res = mid
            l1 = mid + 1
        elif val < l2:
            l1 = mid + 1
        else:
            r1 = mid - 1
    return res

for t in range(tc):
    k,l1,r1,l2,r2 = [int(x) for x in input().split(" ")]
    powers = [k**i for i in range(33)]
    res = 0
    for n in range(33):
        upper = ubs(l1,r1,l2,r2,n,powers)
        lower = lbs(l1,upper,l2,r2,n,powers)
        if lower != -1 and upper != -1:
            res += upper - lower + 1
    print(res)