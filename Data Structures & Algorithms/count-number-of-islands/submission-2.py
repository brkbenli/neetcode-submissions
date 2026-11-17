class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        seen = set()
        def dfs(row, col):

            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or (row, col) in seen or grid[row][col] != "1":
                return
            seen.add((row, col))
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

                
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in seen:
                    dfs(row, col)
                    count += 1
        return count