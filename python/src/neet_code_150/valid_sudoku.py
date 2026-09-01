from typing import List, Dict, Set

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validation: Dict[str, Set[int]] = dict()
        i: int = 0
        while i < 9:
            validation["row"+str(i)] = set()
            validation["col"+str(i)] = set()
            validation["sqr"+ str(i)] = set()
            i += 1

        row: int = 0
        col: int = 0
        while row < 9:
            col = 0
            while col < 9:
                if board[row][col] != ".":
                    value: str = board[row][col]
                    if value in validation["row"+str(row)]:
                        return False
                    if value in validation["col"+str(col)]:
                        return False
                    if value in validation["sqr"+str((int(row/3) * 3) + int((col / 3)))]:
                        return False
                    
                    validation["row"+str(row)].add(value)
                    validation["col"+str(col)].add(value)
                    validation["sqr"+str((int(row/3) * 3) + int((col / 3)))].add(value)
                col += 1
            row += 1
        
        return True
        
        

s = Solution()
print(s.isValidSudoku(board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))

print(s.isValidSudoku(board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))