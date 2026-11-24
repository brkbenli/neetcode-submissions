class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols = set()
        posDag = set()
        negDag = set()
        placedQueens = set()
        res = []
        sol = [["."] * n for i in range(n)]
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in sol])
                return
            
            for c in range(n):
                if c in cols or (c + r) in posDag or (r - c) in negDag:
                    continue
                posDag.add(c + r)
                cols.add(c)
                negDag.add(r - c)
                sol[r][c] = "Q"

                backtrack(r + 1)
                
                posDag.remove(c + r)
                cols.remove(c)
                negDag.remove(r - c)
                sol[r][c] = "."
        backtrack(0)
        return res
                    

            
                
            
