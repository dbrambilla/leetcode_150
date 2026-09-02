from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:       
        parent: List[int] = list(range(n))

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

        def compress():
            for i in range(len(parent)):
                if parent[i] != i:
                    parent[i] = find(parent[i])

        for u, v in edges:
            union(u, v)
        compress()

        return len(set(parent))
    
s = Solution()

print(s.countComponents(n = 5, edges = [[0,1],[1,2],[3,4]]))