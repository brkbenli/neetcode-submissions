class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            print(stack)
            if i == "*":
                a, b = stack.pop(), stack.pop()
                newVal = int(b) * int(a)
                stack.append(newVal)
            elif i == "+":
                a, b = stack.pop(), stack.pop()
                newVal = int(b) + int(a)
                stack.append(newVal)
            elif i == "-":
                a, b = stack.pop(), stack.pop()
                newVal = int(b) - int(a)
                stack.append(newVal)
            elif i == "/":
                print(stack, "hi")
                a, b = stack.pop(), stack.pop()
                newVal = int(b) / int(a)
                stack.append(int(newVal))
                print(stack, "hi2")

            else:
                stack.append(i)
        return int(stack.pop())