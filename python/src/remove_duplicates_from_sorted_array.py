from types import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return len(nums)
        
        l: int = 0
        r: int = 1
        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            r += 1
            while r < len(nums) and nums[r] == nums[r-1]:
                r += 1
        
        return l + 1