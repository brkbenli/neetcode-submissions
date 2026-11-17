class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "*", "-", "/"]
        total = 0
        for i in tokens:
            if i not in operators:
                stack.append(i)
                print(stack)
            else:
                total += int(eval(f"{stack[0]} {i} {stack[-1]}"))
        return total