import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        # Heaps and lazy deletion tracking
        small = []  # Max-heap (stores negative numbers)
        large = []  # Min-heap
        delayed = defaultdict(int)  # Tracks elements queued for deletion
        
        # Balance variables to keep track of valid elements in heaps
        small_size = 0
        large_size = 0
        
        def add(num):
            nonlocal small_size, large_size
            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size += 1
            else:
                heapq.heappush(large, num)
                large_size += 1
            rebalance()

        def remove(num):
            nonlocal small_size, large_size
            delayed[num] += 1
            if num <= -small[0]:
                small_size -= 1
            else:
                large_size -= 1
            rebalance()

        def rebalance():
            nonlocal small_size, large_size
            # small can have at most 1 more element than large
            if small_size > large_size + 1:
                heapq.heappush(large, -heapq.heappop(small))
                small_size -= 1
                large_size += 1
                prune()
            elif small_size < large_size:
                heapq.heappush(small, -heapq.heappop(large))
                small_size += 1
                large_size -= 1
                prune()

        def prune():
            # Remove elements from top of heaps if they are marked for deletion
            while small and delayed[-small[0]] > 0:
                delayed[-small[0]] -= 1
                heapq.heappop(small)
            while large and delayed[large[0]] > 0:
                delayed[large[0]] -= 1
                heapq.heappop(large)

        def get_median():
            if k % 2 == 1:
                return float(-small[0])
            else:
                return (-small[0] + large[0]) / 2.0

        # Initialize the first window
        for i in range(k):
            add(nums[i])
            
        result = [get_median()]
        
        # Slide the window
        for i in range(k, len(nums)):
            add(nums[i])          # Add incoming element
            remove(nums[i - k])   # Track outgoing element
            prune()               # Keep tops clean
            result.append(get_median())
            
        return result
