from collections import Counter
s = input()
n = len(s)
c = Counter(s)

def perm(ans,cc):
    if len(ans) == n:
        return ["".join(ans)]
    res = []
    for k in cc:
        if cc[k]:
            ans.append(k)
            cc[k] -= 1
            res.extend(perm(ans,cc))
            ans.pop()
            cc[k] += 1
    
    return res

res = sorted(perm([],c))
print(len(res))
for x in res:
    print(x)