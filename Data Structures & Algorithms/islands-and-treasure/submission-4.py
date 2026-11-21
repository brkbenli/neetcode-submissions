class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def bfs(queue):
            
            seen = set()
            count = 0
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    if (x, y) in seen or x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == -1:
                        continue

                    if count < grid[x][y]:
                        grid[x][y] = count
                    seen.add((x, y))
                    queue.append((x - 1, y))
                    queue.append((x + 1, y))
                    queue.append((x, y - 1))
                    queue.append((x, y + 1))
                count += 1
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))

        bfs(queue)

        
                
                
                
                