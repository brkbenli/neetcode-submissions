class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        def bfs(queue):

            count = 0
            changed = set()

            while queue:
                print(queue)
                newOra = False
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    if (x, y) in changed or x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                        continue
                    
                    changed.add((x, y))
                    grid[x][y] = 2
                    newOra = True
                    queue.append((x - 1, y))
                    queue.append((x + 1, y))
                    queue.append((x, y - 1))
                    queue.append((x, y + 1))
                if newOra:
                    count += 1
            return count
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))

        count = bfs(queue)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return 0 if count - 1 < 0 else count - 1