from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands: int = 0
        def explore(grid: List[List[str]], row: int, col: int):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return
            
            if grid[row][col] == "1":
                grid[row][col] = "0"
                for move_row, move_col in [[-1, 0],[1, 0],[0, -1],[0, 1]]:
                    
                        explore(grid, row + move_row, col + move_col)
                
            return

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    islands += 1
                    explore(grid, row, col)

        return islands


s = Solution()

print(s.numIslands(grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]))