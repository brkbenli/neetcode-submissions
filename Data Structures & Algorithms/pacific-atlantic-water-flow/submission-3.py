class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [(1,0), (0,1), (-1, 0), (0, -1)]
        def dfsPacific(row, col):   
            stack = []
            stack.append((row, col))
            visited = set()
            while stack:
                x, y = stack.pop()
                if (x, y) in visited:
                    continue
                visited.add((x,y))
                for dx, dy in dirs:
                    if x + dx >= 0 and y + dy >= 0 and x + dx < len(heights) and y + dy < len(heights[0]) and heights[x][y] >= heights[x + dx][y + dy]:
                        stack.append((x + dx, y + dy))
                if x == 0 or y == 0:
                    return True
            return False

        def dfsAtlantic(row, col):

            stack = []
            stack.append((row, col))
            visited = set()
            while stack:
                print(stack)
                x, y = stack.pop()
                if (x, y) in visited:
                    continue
                visited.add((x,y))
                print(x, y)
                for dx, dy in dirs:
                    if x + dx >= 0 and y + dy >= 0 and x + dx < len(heights) and y + dy < len(heights[0]) and heights[x][y] >= heights[x + dx][y + dy]:
                        stack.append((x + dx, y + dy))
  
                if x == len(heights) - 1 or y == len(heights[0]) - 1:
                    return True
            return False

        
        valid = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                pac = dfsPacific(row, col)
                atl = dfsAtlantic(row, col)
                if pac and atl:
                    valid.append([row, col])
        return valid        
