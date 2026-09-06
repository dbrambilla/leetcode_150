from typing import List

class Solution:
    """
    X ^ X = 0
    so the same number twice in XOR cancel all the bits
    X ^ 0 = X
    00,11 -> 0
    10, 01 -> 1
    """
    def singleNumber(self, nums: List[int]) -> int:
        result: int = 0
        for num in nums:
            result = result ^ num
        return result
    
s = Solution()

print(s.singleNumber([1,2,1]))