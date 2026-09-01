from ds import TreeNode
from typing import Optional, List
from utils import build_tree_from_list, visualize_tree, visualize_tree_from_array

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            
            return (node1.val == node2.val) and dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
        
        return dfs(q,p)

s = Solution()
tree1 = build_tree_from_list([1,None,2,3,4,5])
tree2 = build_tree_from_list([1,None,2,3])
visualize_tree(tree1)
visualize_tree(tree2)
print(s.isSameTree(tree1, tree2))
