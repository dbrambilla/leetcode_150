from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r  = 0, len(numbers) - 1
        while l < r:
            lv = numbers[l]
            rv = numbers[r]

            if lv + rv == target:
                return [l+1, r+1]
            elif lv + rv < target:
                l += 1
            else:
                r -= 1

        return []
    
s = Solution()
print(s.twoSum(numbers = [1,2,3,4], target = 3))