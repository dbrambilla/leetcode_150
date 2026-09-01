from ds import TreeNode
from typing import Optional, List
from utils import build_tree_from_list, visualize_tree, visualize_tree_from_array

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
 
        return self.dfs(root, 0, targetSum)

    def dfs(self, node: TreeNode, running_sum: int, target: int) -> bool:
        if not node:
            return False
        
        found: bool = False
        if not node.left and not node.right:
            if node.val + running_sum == target:
                return True
    
        if node.left:
            found = self.dfs(node.left, running_sum + node.val, target)
        if node.right:
            return found or self.dfs(node.right, running_sum + node.val, target)
        return found
        

s = Solution()

arr = [5,4,8,11,None,13,4,7,2,None,None,None,1]
arr = [-2,None,-3]
tree = build_tree_from_list(arr)
visualize_tree(tree)
print(s.hasPathSum(tree, -5))

