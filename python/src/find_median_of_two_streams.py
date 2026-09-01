import heapq

class MedianFinder:
    def __init__(self):
        # Max-Heap to store the smaller half (values inverted)
        self.max_heap = []
        # Min-Heap to store the larger half
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # 1. Decide which heap to insert the new number into
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
            
        # 2. Rebalance if the length difference is greater than 1
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        # If one heap has more elements, its top element is the median
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        elif len(self.min_heap) > len(self.max_heap):
            return float(self.min_heap[0])
        
        # If heaps are of equal size, the median is the average of both tops
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0