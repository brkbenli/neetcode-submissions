class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            midrow = (top + bot) // 2
            if target > matrix[midrow][-1]:
                top = midrow + 1
            elif target < matrix[midrow][0]:
                bot = midrow - 1
            else:
                break
        if not (top <= bot):
            return False


        left, right = 0, COLS - 1
        while left <= right:
            midval = (left + right) // 2
            if matrix[midrow][midval] > target:
                left = midval + 1
            if matrix[midrow][midval] < target:
                right = midval - 1
            else:
                return True
        return False