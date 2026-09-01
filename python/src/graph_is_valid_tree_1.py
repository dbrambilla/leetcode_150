class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # Quick edge count check
        if len(edges) != n - 1:
            return False
            
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i]) # Path compression
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False # Cycle detected if roots match
            
        for u, v in edges:
            if not union(u, v):
                return False
                
        return True
