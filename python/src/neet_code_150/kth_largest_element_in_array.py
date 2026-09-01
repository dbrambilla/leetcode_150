from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # els = set()
        heap = []

        for num in nums:
            # if num in els:
            #     continue
            
            heapq.heappush(heap, num)
            # els.add(num)

            if len(heap) > k:
                val = heapq.heappop(heap)
                # els.remove(val)

        return heap[0]
    
s = Solution()
print(s.findKthLargest(nums=[2,3,1,1,5,5,4], k=3))
print(s.findKthLargest(nums = [2,3,1,5,4], k = 2))