from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROTTEN, EMPTY, FRESH = 2, 0, 1
        queue: deque = deque()
        fresh_fruits: int = 0
        visited: List[List[bool]] = []

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                visited.append([False] * len(grid[0]))
                if grid[row][col] == ROTTEN:
                    queue.append([row, col])
                if grid[row][col] == FRESH:
                    fresh_fruits += 1

        time: int = 0
        while fresh_fruits > 0 and queue:
            time += 1
            size: int = len(queue)
            for i in range(size):
                row,col = queue.popleft()
                grid[row][col] = ROTTEN
                for move_row, move_col in [[-1,0],[1,0],[0,-1],[0,1]]:
                    next_row = row + move_row
                    next_col = col + move_col
                    if next_row < 0 or next_row >= len(grid) or next_col < 0 or next_col >= len(grid[0]):
                        continue
                    if grid[next_row][next_col] == FRESH and not visited[next_row][next_col]:
                        fresh_fruits -= 1
                        visited[next_row][next_col] = True
                        queue.append([next_row, next_col])
        
        return time if fresh_fruits == 0 else -1


s = Solution()

print(s.orangesRotting([[1,1,0],[0,1,1],[0,1,2]]))
print(s.orangesRotting([[1,2]]))
print(s.orangesRotting([[1,0,1],[0,2,0],[1,0,1]]))
