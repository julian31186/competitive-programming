tc = int(input())

for t in range(tc):
    R,C = [int(x) for x in input().split(" ")]
    top_pre = [[0 for _ in range(C)] for _ in range(R)]
    bot_pre = [[0 for _ in range(C)] for _ in range(R)]
    res = [0,0,0]

    a = []
    for i in range(R):
        a.append(list(input()))
    
    for i in range(R):
        for j in range(C):
            if i > 0:
                top_pre[i][j] += top_pre[i - 1][j] + (a[i][j] == '#')
            else:
                top_pre[i][j] += (a[i][j] == '#')

    for i in range(R - 1, -1, -1):
        for j in range(C - 1, -1, -1):
            if i < (R - 1):
                bot_pre[i][j] += bot_pre[i + 1][j] + (a[i][j] == "#")
            else:
                bot_pre[i][j] += (a[i][j] == "#")

    for i in range(R):
        for j in range(C):
            if top_pre[i][j] == bot_pre[i][j]:
                if top_pre[i][j] > res[0]:
                    res[0] = top_pre[i][j]
                    res[1] = i
                    res[2] = j
    
    print(f'{res[1] + 1} {res[2] + 1}')