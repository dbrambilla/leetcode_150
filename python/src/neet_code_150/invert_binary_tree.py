from ds import TreeNode
from typing import Optional
from utils import build_tree_from_list, visualize_tree, visualize_tree_from_array

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node: TreeNode):
            if not node:
                return

            node.left, node.right = node.right, node.left
            invert(node.left)
            invert(node.right)

        invert(root)
        return root
    
s = Solution()
tree = build_tree_from_list([1,2,3,4,5,6,7])
visualize_tree(tree)
visualize_tree(s.invertTree(tree))