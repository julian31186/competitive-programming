n = int(input())
total = ((n * (n + 1)) // 2)
h = total // 2

if total % 2 != 0:
    print("NO")
else:
    res = 0
    s1,s2 = set(),set()
    for i in range(n, 0, -1):
        if res + i <= h:
            res += i
            s1.add(i)
    for i in range(1,n + 1):
        if i not in s1:
            s2.add(i)
    
    print("YES")
    print(len(s1))
    for x in s1: print(x)
    print(len(s2))
    for x in s2: print(x)