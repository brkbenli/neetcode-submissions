class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        seen = set()
        def dfs(i, j):
            if (i, j) in seen or i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] == "0":
                return

            seen.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    if (row, col) not in seen:
                        dfs(row, col)
                        count += 1
        return count