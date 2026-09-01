from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        
        i: int = len(temperatures) - 1
        res = [0] * len(temperatures)
        stack = []
        
        while i >= 0:
            v = temperatures[i]
            days: int = 0
            while stack and stack[-1][0] <= v:
                stack.pop()
            if stack and stack[-1][0] > v:
                res[i] = stack[-1][1] - i
            stack.append([v, i])
            i -= 1

        return res
    

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))