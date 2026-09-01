from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited: List[List[bool]] = []
        for i in range(len(board)):
            visited.append([False] * len(board[0]))
        
        def check(index: int, row: int, col: int):
            nonlocal visited, board, word
            if index == len(word):
                return True
        
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
        
            found: bool = False
            if board[row][col] == word[index] and not visited[row][col]:
                visited[row][col] = True
                found = check(index + 1, row + 1 , col) or \
                check(index + 1, row - 1 , col) or \
                check(index + 1, row  , col + 1) or \
                check(index + 1, row , col - 1)
                visited[row][col] = False
                
            return found

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    if check(0, row, col):
                        return True
        
        return False

s = Solution()
print(s.exist(board=[["C","A","A"],["A","A","A"],["B","C","D"]], word="AAB"))
print(s.exist(board=[["A"]], word="A"))
print(s.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCB"))

print(s.exist(
    board = [
        ["A","B","C","D"],
        ["S","A","A","T"],
        ["A","C","A","E"]
    ], word = "CAS")
)