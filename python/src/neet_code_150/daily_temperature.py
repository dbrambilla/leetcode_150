from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[(int, int)] = []
        i: int = len(temperatures) - 1
        result: List[int] = [0] * len(temperatures)

        while i >= 0:
            value: int = temperatures[i]
            if not stack:
                result[i] = 0
                stack.append((value, i))
            else:
                while stack and stack[-1][0] <= value:
                    stack.pop()
                if stack and stack[-1][0] > value:
                    result[i] = stack[-1][1] - i
                stack.append((value, i))
            i -= 1

        return result        

s = Solution()

print(s.dailyTemperatures(temperatures = [30,38,30,36,35,40,28]))