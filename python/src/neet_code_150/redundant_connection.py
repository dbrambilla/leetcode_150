from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent: List[int] = list(range(len(edges) + 1))

        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(a: int, b: int) -> bool:
            parent_a: int = find(a)
            parent_b: int = find(b)
            if parent_a != parent_b:
                parent[parent_a] = parent_b
                return True
            return False

        for u, v in edges:
            if not union(u, v):
                return [u, v]
            
s = Solution()

print(s.findRedundantConnection(edges = [[1,2],[1,3],[3,4],[2,4]]))