class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        seen = set()
        def dfs(row, col):
            stack = []
            stack.append((row, col))
            seen.add((row, col))

            while stack:
                currRow, currCol = stack.pop()
                print(currRow, currCol)
                if currRow - 1 >= 0 and grid[currRow - 1][currCol] == "1" and (currRow - 1, currCol) not in seen:
                    stack.append((currRow - 1, currCol))
                    seen.add((currRow - 1, currCol))
                if currRow + 1 < len(grid) and grid[currRow + 1][currCol] == "1" and (currRow + 1, currCol) not in seen:
                    stack.append((currRow + 1, currCol))
                    seen.add((currRow + 1, currCol))
                if currCol - 1 >= 0 and grid[currRow][currCol - 1] == "1" and (currRow, currCol - 1) not in seen:
                    stack.append((currRow, currCol - 1))
                    seen.add((currRow, currCol - 1))
                if currCol + 1 < len(grid[0]) and grid[currRow][currCol + 1] == "1" and (currRow, currCol + 1) not in seen:
                    stack.append((currRow, currCol + 1))
                    seen.add((currRow, currCol + 1))
                print(stack)
                print(seen)
                

                
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in seen:
                    dfs(row, col)
                    count += 1
        return count