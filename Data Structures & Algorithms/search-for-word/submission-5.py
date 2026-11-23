class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        seen = set()
        def backtrack(r, c, i):
            if i == len(word):
                return True

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or (r, c) in seen:
                return False


            if board[r][c] != word[i]:
                return False
            
            seen.add((r, c))
            res = backtrack(r - 1, c, i + 1) or backtrack(r + 1, c, i + 1) or backtrack(r, c + 1, i + 1) or backtrack(r, c - 1, i + 1)

            seen.remove((r, c))
            
            return res

        found = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    found = True

        return found

            


            
