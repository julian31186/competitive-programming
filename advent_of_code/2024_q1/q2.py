from collections import defaultdict

f = open("input.txt")
res,x,y,c = 0,[],[],defaultdict(int)
for line in f:
    l = line.split("  ")
    n1,n2 = int(l[0].strip()),int(l[1].strip())
    x.append(n1)
    c[n2] += 1

x.sort()

for n in x:
    res += (n * c[n])

print(res)