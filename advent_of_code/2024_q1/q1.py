f = open("input.txt")
res,x,y = 0,[],[]
for line in f:
    l = line.split("  ")
    x.append(int(l[0].strip()))
    y.append(int(l[1].strip()))

x.sort()
y.sort()

for a,b in zip(x,y):
    res += abs(a - b)

print(res)