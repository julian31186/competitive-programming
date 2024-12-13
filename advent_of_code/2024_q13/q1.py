from functools import cache
import math

f = open("input.txt")
res = 0
ax,ay,bx,by,gx,gy = 0,0,0,0,0,0

@cache
def dp(x,y,ax,ay,bx,by,gx,gy,alvl,blvl):
    if x == gx and y == gy:
        return 0
    if x > gx or y > gy or alvl == 100 or blvl == 100: 
        return math.inf
    return min(
        3 + dp(x + ax, y + ay, ax, ay, bx, by, gx, gy, alvl + 1, blvl),
        1 + dp(x + bx, y + by, ax, ay, bx, by, gx, gy, alvl, blvl + 1)
    )

for row in f:
    row_split = row.split(":")

    if row_split[0] == "Button A":
        right = row_split[1].strip().split(", ")
        ax = int(right[0].split("+")[1])
        ay = int(right[1].split("+")[1])
    elif row_split[0] == "Button B":
        right = row_split[1].strip().split(", ")
        bx = int(right[0].split("+")[1])
        by = int(right[1].split("+")[1])
    elif row_split[0] == "Prize":
        right = row_split[1].strip().split(", ")
        gx = int(right[0].split("=")[1])
        gy = int(right[1].split("=")[1])
    else:
        x = dp(0, 0, ax, ay, bx, by, gx, gy, 0, 0)
        res += x if x != math.inf else 0

print(res)
