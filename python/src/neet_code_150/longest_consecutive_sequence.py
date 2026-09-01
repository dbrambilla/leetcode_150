from typing import List, Dict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache: Dict[int, int] = dict()
        m: int = 0

        for num in nums:
            prev: int = num - 1
            next: int = num + 1
            left_len: int = 0
            right_len: int = 0

            if num in cache:
                continue

            if prev in cache:
                left_len = cache[prev]
            if next in cache:
                right_len = cache[next]

            length: int = right_len + left_len + 1
            cache[num - left_len] = length
            cache[num + right_len] = length
            cache[num] = length 
            m = max(m, length)
        
        return m
    
s = Solution()

print(s.longestConsecutive([0,3,2,5,4,6,1,1]))