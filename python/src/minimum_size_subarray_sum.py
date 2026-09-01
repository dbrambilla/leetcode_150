from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1 if nums[0] >= target else 0
        
        l: int = 0
        r: int = 1
        res: int = 1 if nums[l] >= target else 10000000
        curr_sum: int = nums[0]

        while r < len(nums):
            curr_sum += nums[r]
            if curr_sum >= target:
                res = min(res, r - l + 1)
                while curr_sum >= target:
                    curr_sum -= nums[l]
                    res = min(res, r - l + 1)
                    l += 1
            r += 1
        
        return res if res != 10000000 else 0
    
s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
print(s.minSubArrayLen(4, [1,4,4]))
print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
print(s.minSubArrayLen(4, [6,2,1]))