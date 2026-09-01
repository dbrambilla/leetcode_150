from ds import TreeNode
from typing import Optional, List, Deque
from utils import build_tree_from_list, visualize_tree, visualize_tree_from_array

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # kth smallest
        result: TreeNode = None
        def kth_smallest(node: TreeNode, actual_size:int, k: int) -> int:
            nonlocal result

            if not node:
                return 0
            
            left = kth_smallest(node.left,actual_size, k)
            right = kth_smallest(node.right, actual_size + left + 1, k)

            if actual_size + left + 1 == k:
                result = node

            return left + right + 1
        
        kth_smallest(root, 0, k)
        return result.val
            
s = Solution()
trees = [
    ([2,1,3],1),
    ([2,1,3],2),
    ([2,1,3],3),
]
for tree_list, k in trees:
    tree = build_tree_from_list(tree_list)
    visualize_tree(tree)
    print(s.kthSmallest(tree,k))
        
