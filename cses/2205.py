# '''
# Thinking some form of BFS?

# whats tc

# edge between 2 nodes means they have hamming dist of one (aka xor has 1 bit)
# '''


# n = int(input())
# a = []

# def dfs(i,s):
#     if i == n:
#         print(s)
#         a.append("".join(s))
#         return

#     s.append('0')
#     dfs(i + 1,s)
#     s.pop()

#     s.append('1')
#     dfs(i + 1,s)
#     s.pop()

# dfs(0,[])
# for i in range(len(a)):
#     a[i] = int(a[i],2)

# print([bin(x)[2:] for x in a])

# '''
# 00
# 01
# 11
# 10

# '''