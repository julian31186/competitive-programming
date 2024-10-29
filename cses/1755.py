from collections import Counter
s = input()
c = Counter(s)
if sum(v % 2 != 0 for v in c.values()) > 1: print("NO SOLUTION")
else:
    t = [x[::-1] for x in c.items()]
    a = sorted(t,reverse=True)
    res = [''] * sum(x[0] for x in a)
    odd,oddi,oddv = '',-1,0
    for i,(v,k) in enumerate(a):
        if v % 2 != 0:
            odd,oddi,oddv = k,i,v
            break

    if oddi != -1: a.pop(oddi)

    for i in range(len(a)):
        for j in range(a[i][0] // 2):
            res.append(a[i][1])
    
    print("".join(res + [odd] * oddv + res[::-1]))