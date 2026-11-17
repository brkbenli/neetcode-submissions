class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        seen = set()
        def dfs(row, col):
            
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or (row, col) in seen or grid[row][col] == 0:
                return 0
            
            seen.add((row, col))
            # x = 1

            # x += dfs(row - 1, col)
            # x += dfs(row + 1, col)
            # x += dfs(row, col - 1)
            # x += dfs(row, col + 1)
            return 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)

        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in seen:
                    x = dfs(row, col)
                    maxArea = max(maxArea, x)

        return maxArea