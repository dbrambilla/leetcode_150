from ds import TreeNode
from typing import Optional, List, Deque
from utils import build_tree_from_list, visualize_tree, visualize_tree_from_array

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result: List[List[int]] = []
        q: Deque[TreeNode] = deque()
        q.append(root)        
        
        while q:
            level_size: int = len(q)
            level: List[int] = []
            for i in range(level_size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level)
        return result
    
s = Solution()
trees = [
    build_tree_from_list([1,2,3,4,5,6,7]),
    build_tree_from_list([1]),
    build_tree_from_list([]),
]
for tree in trees:
    visualize_tree(tree)
    print(s.levelOrder(tree))