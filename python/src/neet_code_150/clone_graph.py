from ds import Node
from typing import Optional, Dict, Set
from utils import create_graph, graph_to_adj_list

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        cache: Dict[int, Node] = dict()
        visited: Set[int] = set()

        def bt(node: Node, cache: Dict[int, Node], visited: Set[int]):
            if node.val in visited:
                return cache[node.val]
            
            copy: Node = Node(node.val) if node.val not in cache else cache[node.val]
            visited.add(node.val)
            cache[node.val] = copy

            for n in node.neighbors:
                if n.val not in cache:
                    cache[n.val] = Node(n.val)

                if n not in visited:
                    cache[n.val] = bt(n, cache, visited)

                copy.neighbors.append(cache[n.val])
            return copy
        
        return bt(node, cache, visited)
    
s = Solution()

print(graph_to_adj_list(
    s.cloneGraph(
        create_graph(
            [[2],[1,3],[2]]
        ))
))

