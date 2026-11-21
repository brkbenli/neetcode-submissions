class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()
        def dfs(i, j, checkval, seen):
            if (i, j) in seen or i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0]) or heights[i][j] < checkval:
                return

            seen.add((i, j))
            dfs(i - 1, j, heights[i][j], seen)
            dfs(i + 1, j, heights[i][j], seen)
            dfs(i, j - 1, heights[i][j], seen)
            dfs(i, j + 1, heights[i][j], seen)
        # pacific
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    dfs(i, j, heights[i][j], pacific)
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    dfs(i, j, heights[i][j], atlantic)

        return list(pacific & atlantic)

            
            