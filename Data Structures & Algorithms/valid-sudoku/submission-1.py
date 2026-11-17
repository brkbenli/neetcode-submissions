class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows
        for row in range(len(board)):
            rowset = set()
            for col in range(len(board[0])):
                if board[row][col] in rowset and board[row][col].isdigit():
                    return False
                else:
                    rowset.add(board[row][col])

        # check cols
        for row in range(len(board)):
            colset = set()
            for col in range(len(board[0])):
                print(board[col][row])
                if board[col][row] in colset and board[col][row].isdigit():
                    return False
                else:
                    colset.add(board[col][row])

        # check 3x3
        for square in range(len(board)):
            cornerset = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] in cornerset and board[row][col].isdigit():
                        return False
                    cornerset.add(board[row][col])


        return True
