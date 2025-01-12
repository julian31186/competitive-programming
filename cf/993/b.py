tc = int(input())

for t in range(tc):
    s = input()
    res = []
    for c in reversed(s):
        if c == 'q': res.append('p')
        elif c == 'p': res.append('q')
        else: res.append('w')
    print("".join(res))