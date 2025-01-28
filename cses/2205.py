
n = int(input())

def go(i,prev):
    if i == n: return prev
    prev += prev[::-1]
    for idx in range(len(prev)):
        prev[idx] += "0" if idx < len(prev) // 2 else "1"
    return go(i + 1,prev)

for x in go(1,["0","1"]):
    print(x)