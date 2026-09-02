from typing import List

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parent: List[int] = list(range(n))

        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(a: int, b: int) -> bool:
            parent_a: int = find(a)
            parent_b: int = find(b)
            if parent_a == parent_b:
                return False
            parent[parent_a] = parent_b
            return True

        for u, v in edges:
            if not union(u, v):
                return False    

        return True
    
s = Solution()

print(s.validTree(n = 5, edges = [[0,1],[0,2],[1,2],[3,4]]))
print(s.validTree(n = 5, edges = [[0,1],[1,2],[2,3],[1,3]]))
print(s.validTree(n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]))
