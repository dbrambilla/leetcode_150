from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(tasks: list[str], n: int) -> int:
        # 1. Map frequencies of distinct tasks
        counts = Counter(tasks)
        
        # 2. Store tuples of (-frequency, task_name)
        max_heap = [(-cnt, task) for task, cnt in counts.items()]
        heapq.heapify(max_heap)
        
        # 3. Queue stores tracking triples: (remaining_cnt, task_name, available_time)
        cooldown_queue = deque()
        time = 0
        
        while max_heap or cooldown_queue:
            time += 1
            
            # Pull task back to the available heap if its cooldown expired
            if cooldown_queue and cooldown_queue[0][2] == time:
                rem_cnt, task, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, (rem_cnt, task))
                
            if max_heap:
                # Execute the most frequent available task
                rem_cnt, task = heapq.heappop(max_heap)
                rem_cnt += 1 # Process 1 unit (reduces negative frequency)
                
                # If the task still has instances left, send it to cooldown
                if rem_cnt < 0:
                    cooldown_queue.append((rem_cnt, task, time + n + 1)) 
                    # Note: 'time + n + 1' ensures the exact interval constraint is met
                    
        return time