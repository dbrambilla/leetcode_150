from typing import Optional
from ds import TreeNode
from utils import build_tree_from_list, visualize_tree
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, left: int, right: int):
            if not node:
                return True

            if node.val <= left or node.val >= right:
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root,-math.inf,math.inf)
    
s = Solution()

arrs = [[2,1,3], [5,1,4, None, None,3,6]]
for arr in arrs:
    tree = build_tree_from_list(arr)
    visualize_tree(tree)
    print(s.isValidBST(tree))