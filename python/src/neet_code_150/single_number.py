from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result: int = 0
        for num in nums:
            result = result ^ num
        return result
    
s = Solution()

print(s.singleNumber([1,2,1]))