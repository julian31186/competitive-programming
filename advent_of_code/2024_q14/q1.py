from collections import defaultdict
from itertools import accumulate
import operator

f = open("input.txt")
a = []
c = defaultdict(int)

for row in f:
    split_space = row.split(" ")
    p = split_space[0].split("=")[1].split(",")
    v = split_space[1].split("=")[1].split(",")
    vx,vy = int(v[0]),int(v[1])
    x,y = int(p[0]),int(p[1])
    a.append([[x,y],[vx,vy]])

R,C = 103,101

for _ in range(100):
    for i in range(len(a)):
        x,y = a[i][0]
        vx,vy = a[i][1]
        y += vy
        x += vx
        y %= R
        x %= C
        a[i] = [[x,y],[vx,vy]]

for [x,y],_ in a:
    if x < (C // 2) and y < (R // 2): c[0] += 1
    if x > (C // 2) and y < (R // 2): c[1] += 1
    if x > (C // 2) and y > (R // 2): c[2] += 1
    if x < (C // 2) and y > (R // 2): c[3] += 1


print(list(accumulate(c.values(), operator.mul))[-1])