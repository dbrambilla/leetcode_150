from typing import List, Dict, Set
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph: Dict[int, Set[int]] = {k: set() for k in range(numCourses)}
        ingress_order: Dict[int, int] = {k: 0 for k in range(numCourses)}
        queue: deque = deque()
        result: List = []
        
        for node, dep in prerequisites:
            graph[dep].add(node)
            ingress_order[node] += 1

        for node, order in ingress_order.items():
            if order == 0:
                queue.append(node)

        visited: Set[int] = set()
        while queue:
            node: int = queue.popleft()
            deps: Set[int] = graph[node]
            visited.add(node)
            result.append(node)
            for dep in deps:
                if dep in visited:
                    return False
                ingress_order[dep] -= 1
                if ingress_order[dep] == 0:
                    queue.append(dep)
        
        return result if len(visited) == len(graph) else []
    
s = Solution()

print(s.findOrder(numCourses = 3, prerequisites = [[1,0]]))
