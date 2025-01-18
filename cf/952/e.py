import math

tc = int(input())

def count(a,b,c,x,y,z):
    if a <= x and b <= y and c <= z:
        return (x - a + 1) * (y - b + 1) * (z - c + 1)
    return 0    

for t in range(tc):
    
    x,y,z,k = [int(x) for x in input().split(" ")]
    res = 0

    ROOT = int(math.sqrt(k))
    divs = []
    for i in range(1,ROOT + 1):
        ans = k / i
        if (ans).is_integer():
            divs.append(int(ans))
            divs.append(i)

    for i in range(len(divs)):
        for j in range(len(divs)):
            a,b = divs[i],divs[j]
            if (k % (a*b) != 0): continue
            c = (k / (a*b))
            cnt = int(count(a,b,c,x,y,z))
            res = max(res,cnt)
    print(res)