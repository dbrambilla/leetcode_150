from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Search the row
        l: int = 0
        r: int = len(matrix) - 1
        row: int = -1
        while l <= r:
            m: int = int(l + (r -l) / 2)
            if matrix[m][0] <= target <= matrix[m][-1]:
                row = m
                break
            if matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1

        if row == - 1:
            return False
        if l == len(matrix):
            return False

        # Search within the row
        lc: int = 0
        rc: int = len(matrix[l])

        while lc <= rc:
            mc: int = int(lc + (rc - lc)/2)
            if matrix[row][mc] == target:
                return True
            if matrix[row][mc] > target:
                rc = mc - 1
            else:
                lc = mc + 1

        return False
    
s = Solution()

print(s.searchMatrix(matrix=[[1]], target=2))
print(s.searchMatrix(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10))
print(s.searchMatrix(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10))