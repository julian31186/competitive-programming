class Solution:
    def parseBoolExpr(self, e: str) -> bool:
        c = { "&": operator.and_ , "|": operator.or_, "!": operator.not_, "t": True, "f": False }
        i,op_stack,stack = 0,[],[]

        while i < len(e):
            if e[i] in "!&|":
                op_stack.append(c[e[i]])
                stack.append("(")
            elif e[i] in "tf":
                stack.append(c[e[i]])
            elif e[i] == ")":
                op = op_stack.pop()
                res = None
                while stack[-1] != "(":
                    if res == None: res = stack.pop()
                    else: res = op(res,stack.pop())
                stack.pop()
                stack.append(not res if op == operator.not_ else res)
            i += 1

        return stack[-1]