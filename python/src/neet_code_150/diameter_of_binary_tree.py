from ds import TreeNode
from typing import Optional, List
from utils import build_tree_from_list, visualize_tree, visualize_tree_from_array

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m: int = 0
        
        def dfs(node: TreeNode) -> int:
            nonlocal m
            if not node:
                return 0
            
            left: int = dfs(node.left)
            right: int = dfs(node.right)
            
            m = max(m, left + right)
            
            return 1 + max(left, right)
            

        dfs(root)
        return m
    
s = Solution()
tree = build_tree_from_list([1,None,2,3,4,5])
visualize_tree(tree)
print(s.diameterOfBinaryTree(tree))