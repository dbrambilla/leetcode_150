class Solution:
    class UnionFind:
        def __init__(self, size):
            self.root = list(range(size))
            self.rank = [1] * size

        def find(self, x):
            if x == self.root[x]:
                return x
            # Path compression
            self.root[x] = self.find(self.root[x])
            return self.root[x]

        def union(self, x, y):
            rootX = self.find(x)
            rootY = self.find(y)
            
            if rootX != rootY:
                if self.rank[rootX] > self.rank[rootY]:
                    self.root[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.root[rootX] = rootY
                else:
                    self.root[rootY] = rootX
                    self.rank[rootX] += 1
                return True
            return False

    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        edges = []
        
        # Generate all edges
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
                
        # Sort edges by weight
        edges.sort()
        
        uf = self.UnionFind(n)
        mst_weight = 0
        edges_used = 0
        
        # Kruskal's MST using union-find DS
        for weight, u, v in edges:
            if uf.union(u, v):
                mst_weight += weight
                edges_used += 1
                # Optimization: Stop once we have connected all n points (n-1 edges)
                if edges_used == n - 1:
                    break
                    
        return mst_weight

            
    
s = Solution()

print(s.minCostConnectPoints([[0,0],[2,2],[3,3],[2,4],[4,2]]))
