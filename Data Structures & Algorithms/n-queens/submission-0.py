class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rowSet = set()
        posD = set()
        negD = set()

        res = []
        board = []
        board = [["."] * n for _ in range(n)]
        def dfs(r):
            if r >= n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in rowSet or (r - c) in posD or (r + c) in negD:
                    continue
                rowSet.add(c)
                board[r][c] = "Q"
                posD.add(r - c)
                negD.add(r + c)

                dfs(r + 1)

                board[r][c] = "."
                rowSet.remove(c)
                posD.remove(r - c)
                negD.remove(r + c)

        dfs(0)
        print(res)
        return res