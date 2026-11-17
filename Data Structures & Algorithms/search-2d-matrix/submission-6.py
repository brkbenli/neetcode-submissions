class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # first find row
        l = 0
        r = len(matrix) - 1
        row = None
        while r >= l:
            middle = (l + r) // 2
            if matrix[middle][0] <= target and matrix[middle][-1] >= target:
                row = middle
                break

            elif matrix[middle][-1] < target:
                l = middle + 1
            else:
                r = middle - 1

        l = 0
        r = len(matrix[row]) - 1
        
        while r >= l:
            middle = (l + r) // 2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] > target:
                r = middle - 1

            else:
                l = middle + 1
        return False

        print(row)
