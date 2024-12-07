f = open("input.txt")

res = 0

def dfs(i,acc,goal,nums):
    if i == len(nums):
        return acc == goal
    return dfs(i + 1,acc * nums[i] if acc != 0 else nums[i],goal,nums) or dfs(i + 1,acc + nums[i],goal,nums) or dfs(i + 1,int(str(acc) + str(nums[i])), goal, nums)

for row in f:
    row = row.split(":")

    t = int(row[0])

    nums = [int(x) for x in row[1].strip().split(" ")]
    if dfs(0,0,t,nums): res += t

print(res)