from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def count(piles: List[int], h:int) -> int:
            total: int = 0
            for pile in piles:
                total += math.ceil(pile / h)
            return total

        l: int = 1
        r: int = max(piles)
        optimal: int = sum(piles)
        while l <= r:
            m: int = l + math.ceil((r - l) / 2)
            t: int = count(piles, m)
            if t <= h:
                optimal = min(m, optimal)
                r = m - 1
            else:
                l = m + 1
        return optimal
    
s = Solution()

print(s.minEatingSpeed(piles = [1,4,3,2], h = 9))
print(s.minEatingSpeed(piles=[312884470], h=312884469))
print(s.minEatingSpeed(piles=[30,11,23,4,20], h=6))
print(s.minEatingSpeed(piles=[25,10,23,4], h=4))


