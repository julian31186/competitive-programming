def ra():
    return [int(x) for x in input().split(" ")]

def ri():
    return int(input())

def solve(a,b,c):
    return "Yes" if (a + b > c) and (b + c > a) and (a + c > b) else "No"

print(solve(*ra()))