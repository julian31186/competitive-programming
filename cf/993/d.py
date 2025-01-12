from collections import defaultdict

tc = int(input())

for t in range(tc):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    b = []
    nums = set([x for x in range(1, len(a) + 1)])
    v = set()
    
    for i,x in enumerate(a):
        if x in v:
            tmp = nums.pop()
            b.append(tmp)
            v.add(tmp)
        else:
            v.add(x)
            nums.remove(x)
            b.append(x)
    
    print(*b)
