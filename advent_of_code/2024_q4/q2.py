f = open("input.txt")

arr = []

for row in f:
    a = []
    for c in row:
        a.append(c)
    if a[-1] == "\n": a.pop()
    arr.append(a)

R,C = len(arr),len(arr[0])
res = 0

for i in range(1,R - 1):
    for j in range(1,C - 1):

        if arr[i][j] == "A":
            res += "".join(sorted(arr[i - 1][j - 1] + arr[i][j] + arr[i + 1][j + 1])) == "AMS" and "".join(sorted(arr[i - 1][j + 1] + arr[i][j] + arr[i + 1][j - 1])) == "AMS"

print(res)