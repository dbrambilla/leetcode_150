from typing import List
import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l: int = 0
        r: int = len(nums) - 1
        while l <= r:
            m: int = l + (r - l) // 2     
            if nums[m] == target:
                return m
            
            # Left side sorted
            if nums[m] >= nums[l]:
                if nums[l] <= target and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
            # Right side sorted
                if nums[r] >= target and target >= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
    
s = Solution()

print(s.search(nums = [3,4,5,6,1,2], target = 1)) # 4
