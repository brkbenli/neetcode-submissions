class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        signs = "+-/*"
        stack = []
        output = 0
        for i in range(len(tokens)):
            print(tokens[i])
            if tokens[i] in signs:
                if len(stack) > 1:
                    a, b = stack.pop(), stack.pop()
                    if tokens[i] == "+":
                        c = int(a) + int(b)
                        stack.append(c)
                    elif tokens[i] == "-":
                        c = int(b) - int(a)
                        stack.append(c)
                    elif tokens[i] == "*":
                        c = int(b) * int(a)
                        stack.append(c)
                    else:
                        c = int(b) / int(a)
                        stack.append(c)
            else:
                stack.append(tokens[i])
            print(stack)
            print(i)
        return int(stack.pop())