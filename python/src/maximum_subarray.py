from typing import List
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        
        curr_max: int = nums[0]
        curr_sum: int = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            curr_max = max(curr_max, curr_sum)

        return curr_max
    
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([-2]))
print(s.maxSubArray([1]))
print(s.maxSubArray([5,4,-1,7,8]))
        
