from typing import List
import heapq

"""
We want to run a simulation on the stones as follows:

At each step we choose the two heaviest stones, with weight x and y and smash them togethers
- If x == y, both stones are destroyed
- If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
- Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-v for v in stones]
        heapq.heapify(heap)

        while heap:
            if len(heap) <= 1:
                return -heap[0] if heap else 0
            
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x == y:
                continue
            heapq.heappush(heap, -(max(y,x) - min(y,x)))

        return 0

s = Solution()

print(s.lastStoneWeight([2,3,6,2,4]))