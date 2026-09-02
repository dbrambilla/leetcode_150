from typing import List, Deque, Set, Dict
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        next_node: List[List[int, int]] = []
        visited: Set[int] = set()
        graph: Dict[int, List[List[int, int]]] = defaultdict(lambda: list())
        distances: Dict[int, int] = defaultdict(lambda: math.inf)

        for source, target, time in times:
            graph[source].append([target, time])

        heapq.heappush(next_node,[0, k])
        distances[k] = 0
        min_distance: int = 0
        while next_node:
            _, node = heapq.heappop(next_node)
            if node in visited:
                 continue
            visited.add(node)
            distance = distances[node]
            for child, time in graph[node]:
                distances[child] = min(distance + time, distances[child])
                heapq.heappush(next_node, [time, child])

        return max(distances.values()) if len(visited) == n else -1

s = Solution()

print(s.networkDelayTime(times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1))
        

