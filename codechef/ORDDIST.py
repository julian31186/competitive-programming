tc = int(input())

def solve(n,x,y):
    for i in range(len(x)):
        pivot = x[i]
        xx = []
        for j in range(len(x)):
            xx.append((abs(x[j] - pivot),x[j]))
        xx.sort()
        yy = [tup[1] for tup in xx]
        if y == yy: return i + 1
    return -1

for _ in range(tc):
    n = int(input())
    x,y = [int(x) for x in input().split(" ")],[int(x) for x in input().split(" ")]
    print(solve(n,x,y))
    