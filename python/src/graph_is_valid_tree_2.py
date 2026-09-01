from collections import deque, defaultdict

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if n == 1 and not edges:
            return True
        # This checks is to guarantee that there are not any
        # disconnected subgraphs that can be mistaken for separate trees
        if len(edges) != n - 1:
            return False
            
        # Build adjacency list and track degrees
        adj = defaultdict(list)
        degrees = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
            
        # Push all leaves (degree == 1) to the queue
        queue = deque([i for i in range(n) if degrees[i] == 1])
        processed_nodes = 0
        
        while queue:
            node = queue.popleft()
            processed_nodes += 1
            
            for neighbor in adj[node]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 1:
                    queue.append(neighbor)
                    
        return processed_nodes == n
