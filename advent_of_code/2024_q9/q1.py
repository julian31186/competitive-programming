f = open("input.txt")

s = []
id = -1
l = 0
res = 0

for row in f:
    for i,c in enumerate(row):
        if i % 2 == 0: 
            id += 1
            s += [str(id)] * int(c)
        else:
            s += ['.'] * int(c)

for r in range(len(s) - 1, -1, -1):
    if s[r] == ".": continue
    while l < r and s[l] != ".":
        l += 1
    if l == r: break
    s[l],s[r] = s[r],s[l]

for i in range(len(s)):
    if s[i] == '.': break
    res += (i * int(s[i]))

print(res)