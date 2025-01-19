MOD = 10**9 + 7
n = len(nums)
comb = [[0 for _ in range(k+1)] for _ in range(n+1)]
comb[0][0] = 1
for i in range(1, n+1):
    for j in range(min(k+1, i+1)):
        comb[i][j] = comb[i-1][j]
        if j > 0:
            comb[i][j] += comb[i-1][j-1]
            comb[i][j] %= MOD