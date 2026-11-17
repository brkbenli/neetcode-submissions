class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = []
        def backtrack(close, opn):
            if close == opn == n:
                res.append(sol[:])
                return
            
            if close < opn or close > n or opn > n:
                return

            sol.append("(")
            backtrack(close + 1, opn)
            sol.pop()

            sol.append(")")
            backtrack(close, opn + 1)
            sol.pop()
        backtrack(0, 0)


        output = []
        for i in range(len(res)):
            output.append("".join(res[i]))
        return output
