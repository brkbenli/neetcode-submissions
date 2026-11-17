from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        zeros = set()

        def bfs(row, col):
            graph = set()
            processed = set()
            
            queue = deque()
            count = 0
            queue.append((row, col, count))
            while queue:
                x, y, level = queue.popleft()
                print("hi")
                if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == -1 or (x,y) in processed:
                    continue


                ## change val current cell
                if level < grid[x][y]:
                    grid[x][y] = level
                processed.add((x,y))
                

                dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dx, dy in dirs:
                    queue.append((x + dx, y + dy, level + 1))

                

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    zeros.add((row, col))
        
        for i in zeros:
            x, y = i
            bfs(x, y)
        

        print(zeros)