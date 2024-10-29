nn = int(input())
for k in range(1, nn + 1):
    n = k * k
    total_pairs = ((n) * (n - 1)) // 2
    print(total_pairs - (4 * ((k - 1) * (k - 2))))