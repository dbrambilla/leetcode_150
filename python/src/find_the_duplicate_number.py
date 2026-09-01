from typing import List

class Solution:    
    def findDuplicate(self, nums: List[int]) -> int:
        l: int = 0

        while l < len(nums):
            v = nums[l]
            if v == -1:
                l += 1
                continue
            if v - 1 == l:
                nums[l] = -1
                l += 1
            else:
                while  v - 1 != l:
                    v1 = nums[v-1]
                    if nums[v-1] == -1:
                        return v
                    nums[l] = v1
                    nums[v-1] = -1
                    v = nums[l]
        
s = Solution()
print(s.findDuplicate([1,3,4,2,2]))
print(s.findDuplicate([3,1,3,4,2]))
print(s.findDuplicate([3,3,3,3,3]))
