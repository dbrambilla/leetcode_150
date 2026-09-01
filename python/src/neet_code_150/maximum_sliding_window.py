from collections import deque

class Solution:
    def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
        dq = deque()  # Stores indices
        result = []
        
        for i, num in enumerate(nums):
            # 1. Remove indices that are out of the current window bounds
            if dq and dq[0] < i - k + 1:
                dq.popleft()
                
            # 2. Maintain monotonic decreasing property
            while dq and nums[dq[-1]] <= num:
                dq.pop()
                
            # 3. Add current element's index
            dq.append(i)
            
            # 4. Append max to result once the first window is fully formed
            if i >= k - 1:
                result.append(nums[dq[0]])
                
        return result

            