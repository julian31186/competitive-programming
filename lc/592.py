class Solution:
    def fractionAddition(self, e: str) -> str:
        i,stack = 0,[]
        e += "."
        ops = { "+", "-", "." }

        while i < len(e):
            num,denom = "",""
            while e[i] != "/":
                num += e[i]
                i += 1
            i += 1
            while e[i] not in ops:
                denom += e[i]
                i += 1
            curr = [int(num),int(denom)]
            if stack and stack[-1] in ops and stack[-1] != ".":
                op = stack.pop()
                num1,denom1 = curr
                num2,denom2 = stack.pop()

                if denom1 != denom2:
                    tempd = denom1
                    
                    num1 *= denom2
                    denom1 *= denom2

                    num2 *= tempd
                    denom2 *= tempd

                if op == "+":
                    num2 += num1
                if op == "-":
                    num2 -= num1
                curr = [num2,denom2]
        
            stack.append(curr)
            stack.append(e[i])
            
            i += 1

        neg = False
        num,denom = stack[-2]
        if num < 0:
            neg = True
            num = -num
        check = num
        if (num / denom).is_integer(): return f'{("-" if neg else "") + str(num // denom)}/1'
        while check:
            if num % check == 0 and denom % check == 0:
                return ("-" if neg else "") + str(num // check) + "/" + str(denom // check)
            check -= 1
        return ("-" if neg else "") + str(num) + "/" + str(denom)