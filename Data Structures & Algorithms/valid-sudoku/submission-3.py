class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        for row in range(0, 9):
            seen = set()
            for col in range(0, 9):
                print(seen)
                if board[row][col] in seen and board[row][col] != ".":
                    return False
                else:
                    seen.add(board[row][col])

        for row in range(0, 9):
            seen = set()
            for col in range(0, 9):
                print(seen)
                if board[col][row] in seen and board[col][row] != ".":
                    return False
                else:
                    seen.add(board[col][row])

        


        # 3x3
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for i in range(9):
                    r = row + i // 3
                    c = col + i % 3
                    gridpoint = board[r][c]
                    
                    if gridpoint in seen and gridpoint != ".":
                        return False
                    else:
                        seen.add(gridpoint)
        return True