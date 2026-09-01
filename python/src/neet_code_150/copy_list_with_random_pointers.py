from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def build_linked_list(data: list) -> 'Node':
    if not data:
        return None
        
    # Step 1: Create all Node objects with their values
    nodes = [Node(val) for val, _ in data]
    
    # Step 2: Connect next and random pointers
    for i, (_, rand_idx) in enumerate(data):
        # Connect next pointer (except for the last node)
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
            
        # Connect random pointer using the stored index
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
            
    # Return the head of the list
    return nodes[0]

def print_list(head: 'Node'):
    # Map nodes to indices to format the output like the input
    node_to_idx = {}
    curr = head
    idx = 0
    while curr:
        node_to_idx[curr] = idx
        curr = curr.next
        idx += 1
        
    # Print each node's val and its random target's val
    curr = head
    while curr:
        rand_val = curr.random.val if curr.random else "None"
        print(f"Node(val: {curr.val}, random_points_to: {rand_val})")
        curr = curr.next

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        dummy: Node = Node(0)
        current: Node = dummy
        cache = {}

        while head:
            node: Node = None
            if head in cache:
                node = cache[head]
            else:
                node = Node(head.val) if head else None
                cache[head] = node
            current.next = node
            
            # Next
            next = head.next
            if next in cache:
                node = cache[next]
            else:
                node = Node(next.val) if next else None    
                cache[next] = node
            current.next.next = node 
            
            # Random
            random = head.random
            if random in cache:
                node = cache[random]
            else:
                node = Node(random.val) if random else None    
                cache[random] = node
            current.next.random = node

            current = current.next
            head = head.next

        return dummy.next

s = Solution()

l = build_linked_list([[3,None],[7,3],[4,0],[5,1]])
print_list(s.copyRandomList(l))