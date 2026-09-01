from typing import List
import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point: List[int]) -> int:
            return math.sqrt((0 - point[0])**2 + (0 - point[1])**2)
        heap = []
        
        for point in points:
            heapq.heappush(heap, (-distance(point), point))
            if len(heap) > k:
                heapq.heappop(heap)

        return [v[1] for v in heap]
    
s = Solution()

print(s.kClosest(points = [[0,2],[2,2]], k = 1))
