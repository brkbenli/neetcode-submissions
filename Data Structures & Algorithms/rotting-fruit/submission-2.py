from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        seen = set()
        count1s = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                if grid[row][col] == 1:
                    count1s += 1

        print(count1s)
        minutes = 0
        while queue:
            qLen = len(queue)
            for i in range(qLen):

                row, col = queue.popleft()
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or (row, col) in seen or grid[row][col] == 0:
                    continue
                seen.add((row, col))
                grid[row][col] = 2
                count1s -= 1
                queue.append((row + 1, col))
                queue.append((row - 1, col))
                queue.append((row, col + 1))
                queue.append((row, col - 1))
            print(grid)
            if count1s <= 0:
                break
            
            minutes += 1
        print(grid, minutes)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1

        return minutes + 1

