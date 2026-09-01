from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else - 1
        l: int = 0
        r: int = len(nums) - 1

        while l <= r:
            m: int = int(l + (r - l) / 2)
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
    
s = Solution()

print(s.search(nums=[2,5], target=5))
print(s.search(nums = [-1,0,2,4,6,8], target = 3))
print(s.search(nums = [-1,0,2,4,6,8], target = 4))