# cook your dish here

tc = int(input())

for t in range(tc):
    n = int(input())
    a,b = input(),input()
    diff = 0
    cnt = 0
    for i in range(n):
        if (a[i] == '1') and (b[i] == '1'):
            cnt += 1
        elif a[i] != b[i]:
            diff += 1
    if (cnt % 2) != 0:
        print("YES")
    else:
        print("YES" if diff else "NO")