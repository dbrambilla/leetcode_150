from typing import List
import math
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def compute(grid: List[List[int]], row:int, col:int, path: int):
            path_cell: int = math.inf - 1
            wall_cell: int = -1
            if row < 0 or row >= len(grid) or \
                col < 0 or col >= len(grid[0]):
                return
            
            if grid[row][col] == wall_cell:
                return
            
            if grid[row][col] < path:
                return
            
            grid[row][col] = path
            for move_row, move_col in [[-1,0],[1,0],[0,-1],[0,1]]:
                compute(grid, row + move_row, col + move_col, path + 1)

            return

        # Find all the treasures
        treasure_cell: int = 0
        treasures: List[List[int]] = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == treasure_cell:
                    treasures.append([row, col])

        # From all the treasures BST and for each cell set the value if it is not -1 or math.inf - 1
        for row, col in treasures:
            compute(grid, row, col, 0)

    def islandsAndTreasure_2(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
            nonlocal visit, q
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1

s = Solution()

grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
s.islandsAndTreasure(
    grid
)

print(grid)

grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
s.islandsAndTreasure_2(
    grid
)

print(grid)