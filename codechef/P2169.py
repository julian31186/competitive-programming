# cook your dish here

tc = int(input())

for t in range(tc):
    n = int(input())
    s = input()
    res = []
    for c in s:
        res.append('1' if c == '0' else '0')
    print("".join(res))
    