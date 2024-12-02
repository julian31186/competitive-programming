f = open("input.txt")

def good(arr,inc):
    dec = not inc
    for i in range(len(arr) - 1):
        if dec and arr[i + 1] >= arr[i] or arr[i] - arr[i + 1] > 3: return False
        if inc and arr[i + 1] <= arr[i] or arr[i + 1] - arr[i] > 3: return False
    return True

res = 0
for line in f:
    a = [int(x) for x in line.split(" ")]

    for i in range(len(a)):
        b = []
        for j in range(len(a)):
            if i == j: continue
            b.append(a[j])
        if (good(b,True) or good(b,False)):
            res += 1
            break
        
print(res)