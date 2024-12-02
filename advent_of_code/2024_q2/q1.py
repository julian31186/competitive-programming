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
    res += (good(a,True) or good(a,False))

print(res)