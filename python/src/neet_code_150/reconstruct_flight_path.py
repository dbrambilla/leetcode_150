from typing import List, Dict, Set
from collections import defaultdict
class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Hierholzer's Algorithm. Technically to find an Eulerian Path, a directed graph strictly requires that:
         1. The graph must be entirely connected
         2. Exactly one node has out-degree in-degree = 1 (the starting node)
         3. Exactly one node has in-degree - out-degree = 1 (the ending node)
         4 .All other nodes have in-degree == out-degree

        The problem includes one vital guarantee: "You may assume all tickets form at least one valid itinerary."
        Because a valid itinerary is guaranteed to use every single ticket (edge) exactly once, 
        the problem statement inherently forces the input graph to meet all Eulerian Path prerequisites.
        
        You do not need to check degrees, the input is already mathematically guaranteed to be a valid Eulerian graph.
        
        You are told the starting node is "JFK". If the path is a circuit, JFK works as the start. 
        If the path is a line, JFK is guaranteed to be the single node with an extra out-degree.
        """
        # Step 1: Build the graph from tickets
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
            
        # Step 2: Sort in reverse alphabetical order to comply with requirements
        for src in graph:
            graph[src].sort(reverse=True)
            
        stack = ["JFK"]
        itinerary = []
        
        # Step 3: Execute Hierholzer's Algorithm
        while stack:
            curr = stack[-1]
            if graph[curr]:
                # Pop the lexicographically smallest destination
                next_dst = graph[curr].pop()
                stack.append(next_dst)
            else:
                # Dead end reached, lock it into the itinerary
                itinerary.append(stack.pop())
                
        # Step 4: Reverse to get the correct order
        return itinerary[::-1]
    
    def findItinerary_fails_time_limit(self, tickets: List[List[str]]) -> List[str]:
        EDGES: int = len(tickets) + 1
        result: List[str] = []

        def traverse(
            graph: Dict[str, List[str]], 
            node: str, 
            visited: Set[str], 
            path: List[str]
        ):
            nonlocal result
            if len(path) == EDGES:
                result = path[:]
                return True
            
            for next in graph[node]:
                ticket = node + "#" + next
                if ticket not in visited:
                    visited.add(ticket)
                    path.append(next)
                    if traverse(graph, next, visited, path):
                        return True
                    visited.remove(ticket)
                    path.pop()

            return False

        graph: Dict[str, List[str]] = defaultdict(lambda: list())
        for source, dest in tickets:
            graph[source].append(dest)

        for _, v in graph.items():
            v.sort()

        visited: Set[str] = set()
        path: List[str] = ["JFK"]

        traverse(graph, "JFK", visited, path)
        res = []
        for el in result:
            res.extend(el.split("#"))

        return res

s = Solution()

print(s.findItinerary([["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]))
print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
print(s.findItinerary([["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]))