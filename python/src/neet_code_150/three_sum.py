from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        nums.sort()
        x: int = 0
        while x <= len(nums) - 3:
            if x > 0:
                # Skip any duplicate value
                while x < len(nums) and nums[x] == nums[x-1]:
                    x += 1
            if x == len(nums):
                return result
            target: int = -nums[x]

            l, r  = x + 1, len(nums) - 1
            while l < r:
                lv = nums[l]
                rv = nums[r]

                if lv + rv == target:
                    result.append([nums[x], lv, rv])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                elif lv + rv < target:
                    l += 1
                else:
                    r -= 1
            x += 1
        return result

s = Solution()
print(s.threeSum(nums=[-2,0,0,2,2]))
print(s.threeSum(nums = [0,0,0]))
print(s.threeSum(nums = [0,0,0, 0]))
print(s.threeSum(nums = [-1,0,1,2,-1,-4]))