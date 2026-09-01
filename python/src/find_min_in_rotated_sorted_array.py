from typing import List
import math

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l: int = 0
        r: int = len(nums) - 1
        curr_min: int = nums[0]
        
        while l < r:
            mid = l + ( r - l ) // 2
            if nums[l] < nums[mid]:
                # left side is sorted
                curr_min = min(curr_min, nums[l], nums[mid])
                l = mid + 1
            else:
                # right side is sorted
                curr_min = min(curr_min, nums[mid], nums[r])
                r = mid - 1
        
        return curr_min
    
    def findMin2(self, nums: List[int]) -> int:
        l: int = 0
        r: int = len(nums) - 1
        
        while l < r:
            mid = l + ( r - l ) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
    
s = Solution()

print(s.findMin([4,5,6,7,0,1,2]))
print(s.findMin([3,4,5,1,2]))
print(s.findMin([1]))
print(s.findMin([2,1]))
print(s.findMin([3,2,1]))
print("-------------------")
print(s.findMin2([4,5,6,7,0,1,2]))
print(s.findMin2([3,4,5,1,2]))
print(s.findMin2([1]))
print(s.findMin2([2,1]))
print(s.findMin2([3,2,1]))