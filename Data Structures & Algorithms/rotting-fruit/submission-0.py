from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        
        # find all rotten fruits
        queue = deque()
        twos = set()
        fresh = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    twos.add((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        
        # add 2's to queue and bfs
        minutes = 0
        processed = set()
        while queue and fresh > 0:
            for i in range(len(queue)):
                x, y = queue.popleft()
                print(x, y)
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x, y) in processed or grid[x][y] == 0:
                    continue
                
                processed.add((x, y))
                print(x,y)
                print(queue)
                grid[x][y] = 2
                fresh -= 1

                queue.append((x - 1, y))
                queue.append((x + 1, y))
                queue.append((x, y - 1))
                queue.append((x, y + 1))

            minutes += 1

        print(fresh)


        print(minutes)

        # once finished, final loop to check
        if fresh == 0:
            return minutes
        else:
            return -1
