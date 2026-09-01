from collections import deque
from typing import Optional
from ds import Node

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        visited: Map[int, Node] = {}
        root: Node = Node(1, [])
        curr: Node = root
        visited[1] = curr
        queue: deque = deque([node])    
        while queue:
            n: Node = queue.popleft()
            if n.val not in visited:
                visited[n.val] = Node(n.val, [])
            nn = visited[n.val]

            for nb in n.neighbors:
                if nb.val not in visited:
                    visited[nb.val] = Node(nb.val, [])
                    queue.append(nb)
                nnb = visited[nb.val]
                nn.neighbors.append(nnb)

        return root