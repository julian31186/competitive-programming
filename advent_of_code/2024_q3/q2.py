f = open("input.txt")

def valid(i,row):
    idx = i
    n1,n2 = 0,0
    if row[idx:idx + 3] != "mul": return [False,-1]
    if idx + 3 >= len(row) or row[idx + 3] != "(": return [False,-1]
    idx += 4
    
    while row[idx] != ",":
        if not row[idx].isnumeric(): return [False,-1]
        n1 *= 10
        n1 += int(row[idx])
        idx += 1
    
    idx += 1

    while row[idx] != ")":
        if not row[idx].isnumeric(): return [False,-1]
        n2 *= 10
        n2 += int(row[idx])
        idx += 1
        
    return [True,n1 * n2]

res = 0
toggle = True
for row in f:
    for i in range(len(row) - 2):
        if i + 7 <= len(row) and row[i:i + 7] == "don't()":
            toggle = False
        elif i + 4 <= len(row) and row[i:i + 4] == "do()":
            toggle = True
        
        if toggle:
            x = valid(i,row)
            if x[0]: res += x[1]
        
print(res)