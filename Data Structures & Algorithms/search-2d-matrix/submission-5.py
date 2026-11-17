class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        # find row
        l = 0
        r = len(matrix) - 1
        while r >= l:
            middle = (l + r) // 2
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                break
            elif matrix[middle][0] > target:
                r = middle - 1
            else:
                l = middle + 1
        print(middle)
        # find col
        l = 0
        r = len(matrix[0]) - 1
        while r >= l:
            middle2 = (l + r) // 2
            if matrix[middle][middle2] == target:
                return True
            elif matrix[middle][middle2] > target:
                r = middle2 - 1
            else:
                l = middle2 + 1
        return False
