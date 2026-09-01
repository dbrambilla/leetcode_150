from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        3 = ((()))
            ()(()) ()()()
            (()()) (())()
        """
        result: List[str] = []

        def bt(open: int, close: int, current: str):
            if open == close == 0:
                result.append(current)
                return
            
            if open < 0 or close < 0:
                return

            bt(open - 1, close, current + "(")
            if open < close:
                bt(open, close - 1, current + ")")

        bt(n, n, "")
        return result
    
s = Solution()

print(s.generateParenthesis(3))