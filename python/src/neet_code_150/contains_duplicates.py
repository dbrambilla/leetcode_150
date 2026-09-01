from typing import List, Set

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache: Set[int] = set()
        for num in nums:
            if num in cache:
                return True
            cache.add(num)
        return False
    
s = Solution()

print(s.hasDuplicate([1,2,3,4,5,6]))
print(s.hasDuplicate([1,2,3,4,5,6,1]))
print(s.hasDuplicate([1,2,3,2,3,23]))