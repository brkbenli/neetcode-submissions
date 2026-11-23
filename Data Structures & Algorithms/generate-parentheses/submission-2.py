class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        res = []
        sol = []
        def backtrack(i, openB, closeB):
            if openB == closeB == n:
                res.append(sol[:])

            if closeB > openB:
                return

            if openB < n:
                sol.append("(")
                backtrack(i + 1, openB + 1, closeB)
                sol.pop()

            sol.append(")")
            backtrack(i + 1, openB, closeB + 1)
            sol.pop()

        backtrack(n, 0, 0)
        results = []
        for i in res:
            results.append("".join(i))
        return results