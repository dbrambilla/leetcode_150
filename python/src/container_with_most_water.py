from typing import List

class Solution:
    def maxArea(self, h: List[int]) -> int:
        # If there are only two values the min of the two is the max height
        if len(h) == 2:
            return min(h) # * (1 - 0)
        
        maxh: int = 0
        l: int = 0
        r: int = len(h) - 1

        while l < r: # if the overlap the size would be 0 so cannot be max
            maxh = max(maxh, min(h[l], h[r]) * (r -l))
            if h[l] <= h[r]:
                current_value: int = h[l]
                # We can ignore any value on the right that is lower than this one
                # because we cannot get a better value reducing the length and also
                # reducing the height
                l += 1
                while l < r and h[l] <= current_value:
                    l += 1
            else:
                current_value: int = h[r]
                # We can ignore any value on the left that is lower than this one
                # because we cannot get a better value reducing the length and also
                # reducing the height
                r -= 1
                while l < r and h[r] <= current_value:
                    r -= 1
            
        return maxh
