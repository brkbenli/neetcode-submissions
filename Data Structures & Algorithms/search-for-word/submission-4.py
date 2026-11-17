class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = set()
        def dfs(row, col, i):
            if len(word) == i:
                return True
            if (row < 0 or col < 0 or
                row >= len(board) or col >= len(board[0]) or
                (row, col) in path or
                board[row][col] != word[i]):
                return False

            path.add((row, col))
            
            res = (dfs(row + 1, col, i + 1) or
                    dfs(row - 1, col, i + 1) or 
                    dfs(row, col + 1, i + 1) or
                    dfs(row, col - 1, i + 1)
                    )
            path.remove((row, col))
            return res
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False