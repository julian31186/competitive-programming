from collections import defaultdict

f = open("input.txt")

s = []
id = -1
res = 0

for row in f:
    for i,c in enumerate(row):
        if i % 2 == 0: 
            id += 1
            s += [str(id)] * int(c)
        else:
            s += ['.'] * int(c)

prev = ''
previ = -1
cnt = 0

for r in range(len(s) - 1, -1, -1):
    if s[r] != '.':
        previ = r
        prev = s[r]
        break


for r in range(len(s) - 1, -1, -1):
    if s[r] == ".": continue
    if s[r] != prev:
        
        l,ll = 0,0
        c = defaultdict(int)
        while ll < previ:
            c[s[ll]] += 1
            if ll - l == cnt:
                c[s[l]] -= 1
                if c[s[l]] == 0: del c[s[l]]
                l += 1
            
            if len(c) == 1 and c['.'] == cnt:
                for i in range(l,ll + 1):
                    s[i] = prev
                for i in range(previ, previ + cnt):
                    s[i] = '.'

                break
        
            ll += 1

        prev = s[r]
        previ = r
        cnt = 1
    else:
        previ = r
        cnt += 1

for i in range(len(s)):
    if s[i] == '.': continue
    res += (i * int(s[i]))

print(res)