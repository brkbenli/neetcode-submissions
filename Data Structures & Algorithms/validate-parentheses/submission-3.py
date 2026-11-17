class Solution:
    def isValid(self, s: str) -> bool:
        validP = {"]":"[", ")":"(", "}":"{"}

        opens = "([{"
        stack = []
        for i in s:
            if i in opens:
                stack.append(i)
            else:
                x = stack.pop()
                print(x)
                if validP.get(i) == x:
                    continue
                else:
                    return False

        print(stack)
        return True
                