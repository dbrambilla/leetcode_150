from ds import TreeNode
from typing import Optional, List
from utils import build_tree_from_list, visualize_tree, visualize_tree_from_array

import math

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        valid: bool = True

        def dfs(node: TreeNode) -> int:
            nonlocal valid
            if not node:
                return 0
            
            left: int = dfs(node.left)
            right: int = dfs(node.right)

            if abs(left - right) > 1:
                valid = False

            if not valid:
                return - 1
            
            return 1 + max(left, right)

        dfs(root)
        return valid
    
s = Solution()
trees = [
    build_tree_from_list([1,2,3,None,None,4]),
    build_tree_from_list([1,None,2,3,4,5]),
    build_tree_from_list([1,2,3,None,None,4,None,5])
]
for tree in trees:
    visualize_tree(tree)
    print(s.isBalanced(tree))


