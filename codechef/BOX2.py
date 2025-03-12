def ra():
    return [int(x) for x in input().split(" ")]

def ri():
    return int(input())

tc = ri()

def solve(x,y,k):
    x,y = sorted([x,y])
    n = y - x + 1
    if k > (y + x) or (n % 2) == (k % 2):
        return -1
    return abs(y - x - k) // 2

for _ in range(tc):
    x,y,k = ra()
    print(solve(x,y,k))