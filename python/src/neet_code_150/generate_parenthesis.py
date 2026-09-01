from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def bt(partial:str, result:List[str], open: int, close:int):
            if open == 0 and close == 0:
                result.append("".join(partial))
                return
            
            if open > 0:
                partial.append("(")
                bt(partial, result, open - 1, close)
                partial.pop()
            
            if close > 0 and partial and open < close:
                partial.append(")")
                bt(partial, result, open, close - 1)
                partial.pop()

        result = []
        bt([], result, n, n)
        return result

s = Solution()

print(s.generateParenthesis(3))