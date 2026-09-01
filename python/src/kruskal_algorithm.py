# Kruskal's Algorithm Implementation in Python

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        # Path compression optimization
        self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            # Union by rank optimization
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False

def kruskal(vertices, edges):
    """
    Finds the Minimum Spanning Tree (MST) using Kruskal's Algorithm.
    
    :param vertices: List of all vertex identifiers, e.g., ['A', 'B', 'C', 'D']
    :param edges: List of tuples (weight, u, v) representing edges between u and v
    :return: A tuple containing (mst_edges, total_weight)
    """
    # 1. Sort all edges in non-decreasing order of their weight
    sorted_edges = sorted(edges, key=lambda edge: edge[0])
    
    # 2. Initialize the disjoint-set structure
    ds = DisjointSet(vertices)
    
    mst_edges = []
    total_weight = 0
    expected_mst_edges = len(vertices) - 1

    # 3. Iterate through sorted edges and add if no cycle is formed
    for weight, u, v in sorted_edges:
        if ds.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            
            # Optimization: Stop early if MST contains V-1 edges
            if len(mst_edges) == expected_mst_edges:
                break
                
    return mst_edges, total_weight

# Example usage
if __name__ == "__main__":
    # Define a sample graph
    # Nodes: 0, 1, 2, 3, 4
    graph_vertices = [0, 1, 2, 3, 4]
    
    # Edges format: (weight, node1, node2)
    graph_edges = [
        (1, 0, 1),
        (7, 0, 2),
        (5, 1, 2),
        (4, 1, 3),
        (3, 1, 4),
        (6, 2, 4),
        (2, 3, 4)
    ]
    
    mst, min_cost = kruskal(graph_vertices, graph_edges)
    
    print("Edges in the constructed MST:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == Weight: {weight}")
    print(f"Minimum Spanning Tree Total Weight: {min_cost}")
