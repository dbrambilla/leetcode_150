from collections import deque
from ds import TreeNode

class Codec:
    def serialize(self, root):
        if not root: 
            return ""
        
        queue = deque([root])
        result = []
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("#")
                
        return ",".join(result)

    def deserialize(self, data):
        if not data: 
            return None
        
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        index = 1
        
        while queue:
            parent = queue.popleft()
            
            # Process left child
            if nodes[index] != "#":
                parent.left = TreeNode(int(nodes[index]))
                queue.append(parent.left)
            index += 1
            
            # Process right child
            if nodes[index] != "#":
                parent.right = TreeNode(int(nodes[index]))
                queue.append(parent.right)
            index += 1
            
        return root
