from collections import defaultdict

# cook your dish here

tc = int(input())

for t in range(tc):
    n = int(input())
    a = [int(x) for x in input().split(" ")]

    res = 0
    v = set()
    pre = []
    for i in range(len(a)):
        v.add(a[i])
        pre.append(len(v))

    freq = defaultdict(int)
    c = defaultdict(lambda: [-1,-1])
    for i in range(len(a)):
        freq[a[i]] += 1
        if a[i] not in c:
            c[a[i]][0] = i
        c[a[i]][1] = i

    stack = []
    intervals = sorted(v for k,v in c.items() if freq[k] > 1)
    for i in range(len(intervals)):
        if stack and stack[-1][1] > intervals[i][0]:
            top = stack.pop()
            top[1] = max(top[1],intervals[i][1])
            stack.append(top)
        else:
            stack.append(intervals[i])

    for u,v in stack:
        res += pre[v] - (pre[u - 1] if u - 1 >= 0 else 0)

    print(res)