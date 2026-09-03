from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Given a step you can get there either from a previous
        step or from a two-steps before
        """
        result: List[int] = [0] * (n+1)
        result[0] = 0
        result[1] = 1
        if n > 1:
            result[2] = 2

            for i in range(3, n + 1):
                result[i] = result[i - 1] + result[i - 2]

        return result[n]
    
s = Solution()

print(s.climbStairs(1))
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
print(s.climbStairs(5))