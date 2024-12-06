f = open("input.txt")

a = []
y,x,direc = 0,0,[-1,0]
for i,row in enumerate(f):
    r = []
    for j,c in enumerate(row):
        if c == "^":
            y = i
            x = j
        r.append(c)
    a.append(row)

R,C = len(a),len(a[0])
res = set([(y,x)])

def good():
    return (y >= 0 and y < R and x >= 0 and x < C)

while good():
    y += direc[0]
    x += direc[1]
    if not good(): break
    elif a[y][x] == "#":
        y -= direc[0]
        x -= direc[1]
        if direc == [-1,0]: direc = [0,1]
        elif direc == [0,1]: direc = [1,0]
        elif direc == [1,0]: direc = [0,-1]
        elif direc == [0,-1]: direc = [-1,0]
    else:
        res.add((y,x))

print(len(res))