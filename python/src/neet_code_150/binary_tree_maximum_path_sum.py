from ds import TreeNode
from typing import Optional
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -float('inf')

        def dfs(node):
            if not node:
                return 0
            
            # Post-order: visit children first, ignore if negative
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))
            
            # Update global max considering the current node as the highest turn (vertex)
            self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)
            
            # Propagate only the best single path upwards to the parent
            return node.val + max(left_sum, right_sum)

        dfs(root)
        return self.max_sum

        