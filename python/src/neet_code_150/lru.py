from typing import Dict, List

class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Maps key -> Node
        
        # Initialize sentinel/dummy nodes to avoid null checks
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Removes an existing node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node) -> None:
        """Adds a new node right after the head sentinel (Most Recently Used)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node: Node) -> None:
        """Moves a node to the front of the list (marks as recently used)."""
        self._remove(node)
        self._add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            
            if len(self.cache) > self.capacity:
                # Evict Least Recently Used (LRU) node from the tail
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

def run_lru_cache_simulation(LRUCacheClass, operations_list):
    """Executes LRUCache operations from a single interleaved list."""
    results = []
    cache = None
    
    # Iterate through the list by steps of 2 (Method Name, Arguments)
    for i in range(0, len(operations_list), 2):
        method = operations_list[i]
        args = operations_list[i + 1]
        
        if method == "LRUCache":
            cache = LRUCacheClass(args[0])
            results.append(None)
        elif method == "put":
            cache.put(args[0], args[1])
            results.append(None)
        elif method == "get":
            results.append(cache.get(args[0]))
            
    return results

# --- Your Exact Input List ---
raw_input = [
    "LRUCache", [4], "put", [1, 1], "put", [2, 2], "put", [3, 3], "get", [1], 
    "get", [2], "get", [4], "put", [4, 4], "get", [1], "get", [2], "get", [3], 
    "get", [4], "get", [2], "put", [5, 5], "get", [1], "get", [2], "get", [3], 
    "get", [4], "get", [5], "get", [2], "get", [3], "get", [4], "put", [6,6], 
    "get", [1], "get", [2], "get", [3], "get", [4], "get", [5], "get", [6]
]

# --- Execution ---
output = run_lru_cache_simulation(LRUCache, raw_input)
print(output)
print("[None, None, None, None, 1, 2, -1, None, 1, 2, 3, 4, 2, None, -1, 2, 3, 4, 5, 2, 3, 4, None, -1, 2, 3, 4, -1, 6]")



# lRUCache = LRUCache(2)
# print(lRUCache.put(1, 10))
# print(lRUCache.get(1))
# print(lRUCache.put(2, 20))
# print(lRUCache.put(3, 30))
# print(lRUCache.get(2))
# print(lRUCache.get(1))

# print("-============================-")

# lRUCache = LRUCache(3)
# print(lRUCache.put(1, 1))
# print(lRUCache.put(2, 2))
# print(lRUCache.put(3, 3))
# print(lRUCache.get(1))
# print(lRUCache.get(2))
# print(lRUCache.get(3))
# print(lRUCache.get(4))
# print(lRUCache.put(4, 4))
# print(lRUCache.get(1))
# print(lRUCache.get(2))
# print(lRUCache.get(3))
# print(lRUCache.get(4))

# # "LRUCache", [4], 
# # "put", [1, 1], 
# # "put", [2, 2], 
# # "put", [3, 3], 
# # "get", [1], 
# # "get", [2], 
# # "get", [4], 
# # "put", [4, 4], 
# # "get", [1], 
# # "get", [2], 
# # "get", [3], 
# # "get", [4], 
# # "get", [2], 
# # "put", [5, 5], 
# # "get", [1], 
# # "get", [2], 
# # "get", [3], 
# # "get", [4], 
# # "get", [5], 
# # "get", [2], 
# # "get", [3], 
# # "get", [4], 
# # "put", [6,6], 
# # "get", [1], 
# # "get", [2], 
# # "get", [3], 
# # "get", [4], 
# # "get", [5], 
# # "get", [6]]
