from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l: int = 0
        r: int = 0
        delta: int = 0

        while r < len(prices):          
            val: int = prices[r]
            if val < prices[l]:
                l = r
            delta = max(delta, prices[r] - prices[l])
            r += 1

        return delta
                
s = Solution()

print(s.maxProfit(prices=[5,1,5,6,7,1,10]))