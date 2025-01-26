from collections import defaultdict

# cook your dish here

'''
worst case we can do it in 2 by taking all ones and all zeros
since 0 inversions is divisible by any k and 0 inversions
is always in the range [0,X]

all we need to do is check if we can do it in one
'''

tc = int(input())

for t in range(tc):

    n,x,k = [int(x) for x in input().split(" ")]
    a = input()
    inversions = 0
    c = defaultdict(int)

    for i in range(len(a)):
        if a[i] == '1':
            c['1'] += 1
        else:
            inversions += c['1']

    if (inversions % k == 0) and (0 <= inversions <= x):
        print(1)
    else:
        print(2)