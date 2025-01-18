tc = int(input())

for t in range(tc):
    a = [list(x) for x in input().split(" ")]
    a[0][0],a[1][0] = a[1][0],a[0][0]
    print(f'{"".join(a[0])} {"".join(a[1])}' )