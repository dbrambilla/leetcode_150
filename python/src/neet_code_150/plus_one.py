from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result: List[int] = []
        curry: int = 1
        
        for i in range(len(digits) - 1, -1, -1):
            digit: int = digits[i] + curry
            if digit >= 10:
                curry = 1
                digit -= 10
            else:
                curry = 0
            result.append(digit)
        
        if curry == 1:
            result.append(curry)

        result.reverse()
        return result

s = Solution()

print(s.plusOne([1,2,3,4]))
print(s.plusOne([1,2,3,9]))
print(s.plusOne([9,9,9,9]))