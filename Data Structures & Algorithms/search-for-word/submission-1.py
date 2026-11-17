class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        def dfs(row, col, index):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or (row, col) in visited or board[row][col] != word[index]:
                return False

            visited.add((row, col))

            if index == len(word) - 1:
                return True

            
            u = dfs(row + 1, col, index + 1)
            d = dfs(row - 1, col, index + 1)
            r = dfs(row, col + 1, index + 1)
            l = dfs(row, col - 1, index + 1)

            visited.remove((row, col))
            
            return u or d or r or l
            

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    return dfs(row, col, 0)
        return False

