from typing import List, Dict, Set
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph: Dict[int, Set[int]] = {k: set() for k in range(numCourses)}
        ingress_order: Dict[int, int] = {k: 0 for k in range(numCourses)}
        queue: deque = deque()
        
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
            for dep in deps:
                if dep in visited:
                    return False
                ingress_order[dep] -= 1
                if ingress_order[dep] == 0:
                    queue.append(dep)
        
        return len(visited) == len(graph)
    
s = Solution()

print(s.canFinish(numCourses = 2, prerequisites = [[0,1]]))
print(s.canFinish(numCourses = 2, prerequisites = [[1,0]]))
print(s.canFinish(numCourses = 2, prerequisites = [[0,1],[1,0]]))

