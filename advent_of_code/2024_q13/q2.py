f = open("input.txt")
res = 0
ax,ay,bx,by,tx,ty = 0,0,0,0,0,0
i = 0

for row in f:
    row_split = row.split(":")

    if row_split[0] == "Button A":
        right = row_split[1].strip().split(", ")
        ax = int(right[0].split("+")[1])
        ay = int(right[1].split("+")[1])
    elif row_split[0] == "Button B":
        right = row_split[1].strip().split(", ")
        bx = int(right[0].split("+")[1])
        by = int(right[1].split("+")[1])
    elif row_split[0] == "Prize":
        right = row_split[1].strip().split(", ")
        tx = int(right[0].split("=")[1]) + 10000000000000
        ty = int(right[1].split("=")[1]) + 10000000000000
    else:
        i += 1
        a = ((tx*by) - (ty*bx)) / ((ax*by) - (ay*bx))
        b = (tx - (ax*a)) / bx

        if a.is_integer() and b.is_integer():
            res += 3 * int(a) + int(b)
            
        

print(res)