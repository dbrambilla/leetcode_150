from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Get all O on the edges
        queue: deque = deque()
        
        ROW, COL = len(board), len(board[0])
        for row in range(len(board)):
            if board[row][0] == "O":
                queue.append([row, 0])
            if board[row][COL-1] == "O":
                queue.append([row, COL-1])
        
        for col in range(len(board[0])):
            if board[0][col] == "O":
                queue.append([0, col])
            if board[ROW-1][col] == "O":
                queue.append([ROW-1,col])

        # From there bfs and mark those as Y
        while queue:
            size: int = len(queue)
            for i in range(size):
                row, col = queue.popleft()
                board[row][col] = "Y"
                for r, c in [[-1,0],[1,0],[0,-1],[0,1]]:
                    nr = row + r
                    nc = col + c
                    if nr < 0 or nr >= ROW or nc < 0 or nc >= COL:
                        continue
                    if board[nr][nc] == "O":
                        queue.append([nr, nc])

        # Loop through all the cells
        #   Y -> O
        #   O -> X
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == 'O':
                    board[row][col] = "X"
                if board[row][col] == 'Y':
                    board[row][col] = "O"

s = Solution()

board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]

print(board)
s.solve(board=board)
print(board)