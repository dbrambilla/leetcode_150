import heapq

class MedianFinder:

    def __init__(self):
        self.max_of_mins = []
        self.min_of_maxs = []    

    def addNum(self, num: int) -> None:
        if len(self.max_of_mins) == len(self.min_of_maxs):
            if not self.min_of_maxs or num > -self.max_of_mins[0]:
                heapq.heappush(self.min_of_maxs, num)
            else:
                heapq.heappush(self.max_of_mins, -num)
        elif len(self.max_of_mins) > len(self.min_of_maxs):
            if num > -self.max_of_mins[0]:
                heapq.heappush(self.min_of_maxs, num)
            else:
                heapq.heappush(self.min_of_maxs, -heapq.heappop(self.max_of_mins))
                heapq.heappush(self.max_of_mins, -num)
        else:
            if num < self.min_of_maxs[0]:
                heapq.heappush(self.max_of_mins, -num)
            else:
                heapq.heappush(self.max_of_mins, -heapq.heappop(self.min_of_maxs))
                heapq.heappush(self.min_of_maxs, num)
        return

    def findMedian(self) -> float:
        if len(self.min_of_maxs) == len(self.max_of_mins):
            return (self.min_of_maxs[0] + -self.max_of_mins[0]) / 2
        elif len(self.min_of_maxs) > len(self.max_of_mins):
            return self.min_of_maxs[0]
        return -self.max_of_mins[0]

medianFinder = MedianFinder();
medianFinder.addNum(5)
medianFinder.addNum(3)
print(medianFinder.findMedian())
medianFinder.addNum(7)
print(medianFinder.findMedian())
medianFinder.addNum(2)
print(medianFinder.findMedian())
print("-------------")
medianFinder = MedianFinder();
medianFinder.addNum(1)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())
medianFinder.addNum(2)
print(medianFinder.findMedian())