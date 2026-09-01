from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def explore(grid: List[List[str]], row: int, col: int) -> int:
            size: int = 0
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return size

            if grid[row][col] == 1:
                size += 1    
                grid[row][col] = 0
                for move_row, move_col in [[-1, 0],[1, 0],[0, -1],[0, 1]]:
                    size += explore(grid, row + move_row, col + move_col)
                
            return size

        max_size: int = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_size = max(max_size, explore(grid, row, col))

        return max_size
    
s = Solution()

print(s.maxAreaOfIsland(
    grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]
))