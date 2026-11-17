class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "*", "-", "/"]
        
        for i in tokens:
            if i not in operators:
                stack.append(i)
                print(stack)
            else:
                b = stack.pop()
                a = stack.pop()

                total = eval(f"{a} {i} {b}")
                stack.append(total)
        return stack.pop()