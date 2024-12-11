from functools import cache

f = open("input.txt")
a = []
res = 0

for row in f:
    a = [int(x) for x in row.split(" ")]

@cache
def dfs(i, num):
    if i == 75: return 1
    res = 0
    if num == 0:
        res += dfs(i + 1, 1)
    elif len(str(num)) % 2 == 0:
        res += dfs(i + 1, int(str(num)[:len(str(num)) // 2])) + dfs(i + 1, int(str(num)[len(str(num)) // 2:]))
    else:
        res += dfs(i + 1, num * 2024)
    
    return res

for x in a:
    res += dfs(0,x)

print(res)