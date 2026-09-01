import heapq

class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        # Map each unique start to its original index
        start_to_index = {interval[0]: i for i, interval in enumerate(intervals)}
        
        # 1. Min-heap based on the END of each interval
        # Stores: (end_val, start_val)
        min_heap_end = [(inter[1], inter[0]) for inter in intervals]
        heapq.heapify(min_heap_end)
        
        # 2. Min-heap based on the START of each interval
        # Stores: (start_val, end_val)
        min_heap_start = [(inter[0], inter[1]) for inter in intervals]
        heapq.heapify(min_heap_start)
        
        # Initialize results array with -1
        res = [-1] * len(intervals)
        
        # Loop through heap 1 (sorted by end values)
        while min_heap_end:
            curr_end, curr_start = heapq.heappop(min_heap_end)
            curr_idx = start_to_index[curr_start]
            
            # Pop from heap 2 if its start is strictly less than heap 1's end
            while min_heap_start and min_heap_start[0][0] < curr_end:
                heapq.heappop(min_heap_start)
                
            # If heap 2 still has elements, the top element has the smallest 
            # start value that is >= curr_end
            if min_heap_start:
                match_start = min_heap_start[0][0]
                res[curr_idx] = start_to_index[match_start]
                
        return res
