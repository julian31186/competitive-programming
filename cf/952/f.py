from collections import defaultdict
import math

tc = int(input())

def good(turns,c,boss_health):
    total_dmg = 0
    for _,[dmg,cd] in c.items():
        total_dmg += (dmg * math.ceil(turns / cd))
    return total_dmg >= boss_health

for t in range(tc):
    h,n = [int(x) for x in input().split(" ")]
    
    # [dmg,cd]
    c = defaultdict(lambda: [0,0])
    l,r = 0,2*(10**11)
    res = 0

    for i,dmg in enumerate([int(x) for x in input().split(" ")]):
        c[i][0] = dmg
    for i,cd in enumerate([int(x) for x in input().split(" ")]):
        c[i][1] = cd
    
    while l <= r:
        mid = (r + l) // 2
        if good(mid,c,h):
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    
    print(res)