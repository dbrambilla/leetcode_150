from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l: int = 0
        ml: int = heights[l]
        
        r: int = len(heights) - 1
        mr: int = heights[r]
        
        m: int = min(heights[l], heights[r]) * (r - l)
        
        while l < r:
            if heights[l] < heights[r]:
                l += 1
                while l < r and heights[l] < ml:
                    l += 1
                ml = max(ml, heights[l])
            else:
                r -= 1
                while l < r and heights[r] < mr:
                    r -= 1
                mr = max(mr, heights[r])
            m = max(m, min(heights[l], heights[r]) * (r - l))
        return m
    
s = Solution()

print(s.maxArea(heights = [1,7,2,5,4,7,3,6]))