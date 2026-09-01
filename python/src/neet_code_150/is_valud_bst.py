from ds import TreeNode
from typing import Optional, List, Deque
from utils import build_tree_from_list, visualize_tree, visualize_tree_from_array
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_is_valid(node: TreeNode, path_min: int, path_max:int):
            if not node:
                return True
            
            if path_min >= node.val or path_max <= node.val:
                return False
            
            return check_is_valid(node.left, path_min, node.val) and \
                check_is_valid(node.right, node.val, path_max)

        return check_is_valid(root,-math.inf, math.inf)

s = Solution()
trees = [
    build_tree_from_list([2,2,2]),
    build_tree_from_list([2,1,3]),
    build_tree_from_list([1,2,3]),
    build_tree_from_list([1,2,3,4,5,6,7]),
    build_tree_from_list([1]),
    build_tree_from_list([]),
]
for tree in trees:
    visualize_tree(tree)
    print(s.isValidBST(tree))