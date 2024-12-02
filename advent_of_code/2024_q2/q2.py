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
    inc = any(good(a[:i] + a[i + 1:],True) for i in range(len(a)))
    dec = any(good(a[:i] + a[i + 1:],False) for i in range(len(a)))
    res += (inc or dec)

print(res)