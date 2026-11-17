class Solution:
    def isValid(self, s: str) -> bool:
        parens = {")" : "(", "}" : "{", "]" : "["}

        stack = []
        for i in s:
            if i in parens:
                if stack:
                    if parens[i] == stack.pop():
                        continue
                    else:
                        return False
                else:
                    return False
            stack.append(i)
        return True if not stack else False