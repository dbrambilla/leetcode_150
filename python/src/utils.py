from typing import List, Optional
from ds import TreeNode, ListNode, Node
from collections import deque

def build_tree_from_list(arr: List[Optional[int]]) -> Optional[TreeNode]:
    # Handle empty list case
    if not arr or arr[0] is None:
        return None

    # Create root node and initialize tracking queue
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1  # Pointer to track array position

    while queue and i < len(arr):
        curr_node = queue.popleft()

        # Process left child
        if i < len(arr) and arr[i] is not None:
            curr_node.left = TreeNode(arr[i])
            queue.append(curr_node.left)
        i += 1

        # Process right child
        if i < len(arr) and arr[i] is not None:
            curr_node.right = TreeNode(arr[i])
            queue.append(curr_node.right)
        i += 1

    return root

def visualize_tree_from_array(arr: List[Optional[int]]) -> None:
    """
    Builds and prints a binary tree visually in the terminal from a LeetCode-style array.
    """
    # 1. Reuse the builder logic to convert array to objects
    if not arr:
        print("<Empty Tree>")
        return

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        curr = queue.popleft()
        if i < len(arr) and arr[i] is not None:
            curr.left = TreeNode(arr[i])
            queue.append(curr.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            curr.right = TreeNode(arr[i])
            queue.append(curr.right)
        i += 1

    # 2. Calculate tree height for layout spacing
    def get_height(node):
        return 0 if not node else 1 + max(get_height(node.left), get_height(node.right))

    height = get_height(root)
    
    # 3. BFS-based layout rendering
    current_level = [root]
    for depth in range(height):
        # Calculate dynamic spacing elements
        padding = 2 ** (height - depth - 1) - 1
        between = 2 ** (height - depth) - 1
        
        # Print the nodes for the current level
        node_row = " " * padding
        next_level = []
        for node in current_level:
            if node:
                node_row += f"{node.val}".center(1)
                next_level.extend([node.left, node.right])
            else:
                node_row += " "
                next_level.extend([None, None])
            node_row += " " * between
        print(node_row.rstrip())
        
        # Print the branch connectors for the next level (if it exists)
        if depth < height - 1:
            branch_row = " " * (padding - 1 if padding > 0 else 0)
            for node in current_level:
                if node:
                    left_char = "/" if node.left else " "
                    right_char = "\\" if node.right else " "
                    branch_row += f"{left_char} {right_char}"
                else:
                    branch_row += "   "
                branch_row += " " * (between - 1 if between > 1 else 0)
            print(branch_row.rstrip())
            
        current_level = next_level

def visualize_tree(root: Optional[TreeNode]) -> None:
    """
    Visually prints a binary tree structure in the terminal starting from a TreeNode root.
    """
    if not root:
        print("<Empty Tree>")
        return

    # 1. Helper to calculate tree height for spacing
    def get_height(node: Optional[TreeNode]) -> int:
        return 0 if not node else 1 + max(get_height(node.left), get_height(node.right))

    height = get_height(root)
    current_level = [root]
    
    # 2. Dynamic spacing loop
    for depth in range(height):
        padding = 2 ** (height - depth - 1) - 1
        between = 2 ** (height - depth) - 1
        
        # Render the node values
        node_row = " " * padding
        next_level = []
        for node in current_level:
            if node:
                node_row += f"{node.val}".center(1)
                next_level.extend([node.left, node.right])
            else:
                node_row += " "
                next_level.extend([None, None])
            node_row += " " * between
        print(node_row.rstrip())
        
        # Render the branch connectors for the next row down
        if depth < height - 1:
            branch_row = " " * (padding - 1 if padding > 0 else 0)
            for node in current_level:
                if node:
                    left_char = "/" if node.left else " "
                    right_char = "\\" if node.right else " "
                    branch_row += f"{left_char} {right_char}"
                else:
                    branch_row += "   "
                branch_row += " " * (between - 1 if between > 1 else 0)
            print(branch_row.rstrip())
            
        current_level = next_level

def create_linked_list(arr: list) -> ListNode:
    """Converts a Python list into a linked list and returns the head node."""
    if not arr:
        return None
        
    head = ListNode(arr[0])
    current = head
    
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
        
    return head

def print_linked_list(head: ListNode):
    """Helper method to easily visualize the linked list."""
    elements = []
    current = head
    while current:
        elements.append(str(current.val))
        current = current.next
    print(" -> ".join(elements) if elements else "Empty List")

def create_graph(adjList):
    if not adjList:
        return None
        
    # Dictionary to store created nodes by their 1-indexed value
    nodes = {}
    
    # First pass: Create all node instances
    for i in range(len(adjList)):
        node_val = i + 1
        nodes[node_val] = Node(node_val)
        
    # Second pass: Populate neighbors for each node
    for i, neighbors in enumerate(adjList):
        node_val = i + 1
        current_node = nodes[node_val]
        for neighbor_val in neighbors:
            current_node.neighbors.append(nodes[neighbor_val])
            
    # Return the first node (1-indexed, value 1)
    return nodes[1]

def graph_to_adj_list(root_node: Node) -> List[List[int]]:
    if not root_node:
        return []
        
    # Step 1: Discover all unique nodes using BFS
    visited_nodes = {}
    queue = [root_node]
    visited_nodes[root_node.val] = root_node
    
    while queue:
        current = queue.pop(0)
        for neighbor in current.neighbors:
            if neighbor.val not in visited_nodes:
                visited_nodes[neighbor.val] = neighbor
                queue.append(neighbor)
                
    # Step 2: Determine maximum node value to define the size of the 1-indexed list
    max_val = max(visited_nodes.keys())
    
    # Initialize the adjList structure with empty sublists
    adjList = [[] for _ in range(max_val)]
    
    # Step 3: Populate neighbors into the 1-indexed positions
    for val in range(1, max_val + 1):
        # Handle cases where a node index exists but the node wasn't in the connected component
        if val in visited_nodes:
            node = visited_nodes[val]
            # Extract neighbor integer values
            neighbor_vals = [neighbor.val for neighbor in node.neighbors]
            adjList[val - 1] = neighbor_vals
            
    return adjList