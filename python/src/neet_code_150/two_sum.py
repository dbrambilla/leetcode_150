from typing import List, Dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache: Dict[int, int] = dict()

        for i, num in enumerate(nums):
            check: int = target - num
            if check in cache:
                return [cache[check], i]
            cache[num] = i
        
        return []
    
s = Solution()

print(s.twoSum([3,4,5,6], 7))
print(s.twoSum(nums = [4,5,6], target = 10))
print(s.twoSum(nums = [5,5], target = 10))