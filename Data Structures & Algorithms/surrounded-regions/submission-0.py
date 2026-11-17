class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        # first find outer edge O's and run a dfs and change to #
        def change(string1, string2, row, col):
            stack = []
            stack.append((row, col))
            visited = set()
            while stack:
                x, y = stack.pop()
                if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != "O":
                    continue
                visited.add((x,y))
                board[x][y] = string2
                for dx, dy in dirs:
                    stack.append((x + dx, y + dy))
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row == 0 or col == 0 or row == len(board) - 1 or col == len(board[0]) - 1):
                    change("O", "#", row, col)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    change("O", "X", row, col)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "#":
                    board[row][col] = "O"

        print(board)

        
                         
                        
