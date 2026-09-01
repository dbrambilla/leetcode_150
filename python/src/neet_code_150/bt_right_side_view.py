from ds import TreeNode
from typing import Optional, List, Deque
from utils import build_tree_from_list, visualize_tree, visualize_tree_from_array
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result: List[int] = []
        q: Deque[TreeNode] = deque()
        q.append(root)        
        
        while q:
            level_size: int = len(q)
            for i in range(level_size):
                node = q.popleft()
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return result
    
s = Solution()
trees = [
    build_tree_from_list([1,2,3,4,5,6,7]),
    build_tree_from_list([1]),
    build_tree_from_list([1,2,3,None,4,None,5]),
    build_tree_from_list([1,2,3,4,None, None, None,5]),
    build_tree_from_list([]),
]
for tree in trees:
    visualize_tree(tree)
    print(s.rightSideView(tree))