from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    
kthLargest = KthLargest(3, [1000, -1000]);
print(kthLargest.add(0))
print(kthLargest.add(2))
print(kthLargest.add(-3))
print(kthLargest.add(1000))


kthLargest = KthLargest(1, []);
print(kthLargest.add(3))
print(kthLargest.add(-2))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))

kthLargest = KthLargest(3, [4, 5, 8, 2]);
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))