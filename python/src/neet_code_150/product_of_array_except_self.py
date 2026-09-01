from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left: List[int] = [1] * len(nums)
        right: List[int] = [1] * len(nums)

        i: int = 1
        curr_l: int = 1
        curr_r: int = 1
        while i < len(nums):
            curr_l *= nums[i-1]
            curr_r *= nums[len(nums) - i]
            left[i] = curr_l
            right[len(nums) - i - 1] = curr_r
            i += 1
        
        print(left)
        print(right)

        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])

        return result
    
s = Solution()

print(s.productExceptSelf([1,2,4,6]))