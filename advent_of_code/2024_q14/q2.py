from collections import defaultdict

'''
   *
  >O<
 >@>O<
>O>o<@<
 _| |_

'''

f = open("input.txt")
a = []
c = defaultdict(int)

for row in f:
    split_space = row.split(" ")
    p = split_space[0].split("=")[1].split(",")
    v = split_space[1].split("=")[1].split(",")
    vx,vy = int(v[0]),int(v[1])
    x,y = int(p[0]),int(p[1])
    c[(y,x)] += 1
    a.append([[x,y],[vx,vy]])

R,C = 103,101

def valid(i,j):
    return i >= 0 and j >= 0 and i < R and j < C

for sec in range(10000):
    for i in range(R):
        for j in range(C):
            if c[(i,j)]: print("#",end="")
            else: print(".",end="")
        print()

    for k in range(len(a)):
        x,y = a[k][0]
        vx,vy = a[k][1]
        c[(y,x)] -= 1
        y += vy
        x += vx
        y %= R
        x %= C
        c[(y,x)] += 1
        a[k] = [[x,y],[vx,vy]]
