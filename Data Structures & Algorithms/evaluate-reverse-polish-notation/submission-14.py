class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        opers = ["+", "*", "-", "/"]

        for i in tokens:
            if i in opers:
                x, y = stack.pop(), stack.pop()
                if i == "+":
                    z = int(x) + int(y)
                elif i == "*":
                    z = int(x) * int(y)
                elif i == "-":
                    z = int(y) - int(x)
                else:
                    z = int(y) / int(x)
                stack.append(z)
            else:
                stack.append(i)
        return int(stack[-1])
            