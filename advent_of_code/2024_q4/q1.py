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

for i in range(R):
    for j in range(C):
        deltas = [[-1,0],[-1,-1],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

        for dy,dx in deltas:
            y = i
            x = j

            check = ""

            for k in range(4):
                if not (y >= 0 and y < R and x >= 0 and x < C): break
                check += arr[y][x]
                y += dy
                x += dx
            
            res += check == "XMAS"

print(res)