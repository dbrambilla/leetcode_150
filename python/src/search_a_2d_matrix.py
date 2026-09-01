from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Search rows
        cols: int = len(matrix[0])
        rows: int = len(matrix)

        row: int = 0
        while row < rows:
            if matrix[row][0] <= target <= matrix[row][cols - 1]:
                break
            row += 1
        
        if row == rows: 
            return False

        # Binary search in row
        l: int = 0
        r: int = cols - 1
        while l <= r:
            mid: int = l + (r-l) // 2
            if matrix[row][mid] == target:
                return True

            if matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
    

s = Solution()
print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 16))
