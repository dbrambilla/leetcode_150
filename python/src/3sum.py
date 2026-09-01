
from ast import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Result
        result: List[List[int]] = []

        if len(nums) < 3:
            return result
        
        # Sort the array
        nums.sort()

        # First element of the sum
        i: int = 0
        
        while i <= len(nums) - 3:
            i_value: int = nums[i]

            if i_value > 0:
                return result

            # Perform a 2 sum search 
            l: int = i + 1
            r: int = len(nums)
            while l < r:
                l_value = nums[l]
                r_value = nums[r]
                if i_value + l_value + r_value == 0:
                    result.append([i_value, l_value, r_value])
                    l += 1
                    while l < r and l_value == nums[l - 1]:
                        l += 1
                elif i_value + l_value + r_value > 0:
                    r -= 1
                else:
                    l += 1

            # Skip duplicate values for the first element
            while i > 0 and i < len(nums) - 3 and i_value == nums[i-1]:
                i += 1
        
        return result
            