from ds import TreeNode
from typing import Optional
from utils import build_tree_from_list, visualize_tree, visualize_tree_from_array


from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth: int = 0
        queue = deque()
        queue.append(root)
        while queue:
            depth += 1
            size: int = len(queue)
            for i in range(size):
                node: TreeNode = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth
    
s = Solution()

tree = build_tree_from_list([1, 2, 3, None, None, 4])
visualize_tree(tree)
print(s.maxDepth(tree))

tree = build_tree_from_list([])
visualize_tree(tree)
print(s.maxDepth(tree))